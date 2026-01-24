import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("BTP-Adapter")

def process_sap_odata_payload(raw_data):
    """
    Simulează procesarea unui payload OData v4 provenit din SAP BTP.
    Demonstrează expertiza în structuri de date Enterprise.
    """
    try:
        data = json.loads(raw_data)
        context = data.get("@odata.context")
        items = data.get("value", [])
        
        logger.info(f"OData Context Verified: {context}")
        for item in items:
            logger.info(f"Processing Enterprise Asset ID: {item.get('id')}")
            
        return True
    except Exception as e:
        logger.error(f"OData Parsing Error: {e}")
        return False

# Exemplu de structură OData conformă 2026
sample_payload = '{"@odata.context": "$metadata#Items", "value": [{"id": 101, "name": "BTP Component"}]}'
process_sap_odata_payload(sample_payload)


