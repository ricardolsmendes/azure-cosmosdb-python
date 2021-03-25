# azure-cosmosdb-python

Python samples to help Data Citizens who work with Azure Cosmos DB.

## persist_json_data.py

Used to persist data in the JSON format into Cosmos DB.

### Usage instructions

1. Export the Cosmos endpoint, key, database id, container id, and partition
   key as environment variables:

   ```shell
   export JSON2COSMOS_ENDPOINT=<COSMOS_ENDPOINT>
   export JSON2COSMOS_KEY=<COSMOS_KEY>
   export JSON2COSMOS_DATABASE=<COSMOS_DATABASE>
   export JSON2COSMOS_CONTAINER=<COSMOS_CONTAINER>
   export JSON2COSMOS_PARTITIONKEY=/invoiceId
   ```

1. Run the script:

   ```
   python persist_json_data.py \
     --cosmos-endpoint $JSON2COSMOS_ENDPOINT \
     --cosmos-key $JSON2COSMOS_KEY \
     --cosmos-database $JSON2COSMOS_DATABASE \
     --cosmos-container $JSON2COSMOS_CONTAINER \
     --partition-key $JSON2COSMOS_PARTITIONKEY \
     --data "{\"invoiceId\": \"1030300215\", \"grandTotal\": 28.55}"
   ```
