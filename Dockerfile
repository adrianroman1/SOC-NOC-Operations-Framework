# Stage 1: Build (Optimizat pentru caching)
FROM maven:3.9.6-eclipse-temurin-17-alpine AS build
WORKDIR /app

# Copiem doar pom.xml pentru a descărca dependențele (caching layer)
COPY pom.xml .
RUN mvn dependency:go-offline -B

# Copiem sursele și compilăm
COPY src ./src
RUN mvn clean package -DskipTests -B

# Stage 2: Runtime (Security-Hardened)
FROM eclipse-temurin:17-jre-alpine
WORKDIR /app

# Parametri de optimizare JVM pentru containere
ENV JAVA_OPTS="-XX:+UseParallelGC -XX:MaxRAMPercentage=75.0 -Djava.security.egd=file:/dev/./urandom"

# Securitate: Creăm un user de sistem pentru a evita rularea ca root
RUN addgroup -S btp-group && adduser -S btp-user -G btp-group

# Copiem doar artefactul necesar
COPY --from=build /app/target/*.jar adapter.jar

# Setăm permisiunile corecte
RUN chown btp-user:btp-group adapter.jar

# Switch la user non-root
USER btp-user

EXPOSE 8080

# ENTRYPOINT configurat să accepte parametri externi (pentru Kyma/K8s)
ENTRYPOINT ["sh", "-c", "java $JAVA_OPTS -jar adapter.jar"]
