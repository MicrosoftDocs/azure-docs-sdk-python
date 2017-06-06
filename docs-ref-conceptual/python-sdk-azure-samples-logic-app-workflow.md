
# Create a Logic App Workflow

The following code creates a logic app workflow.

```python
from azure.mgmt.logic.models import Workflow

group_name = 'myresourcegroup'
workflow_name = '12HourHeartBeat'
logic_client.workflows.create_or_update(
    group_name,
    workflow_name,
    Workflow(
        location = 'West US',
        definition={
            "$schema": "https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#",
            "contentVersion": "1.0.0.0",
            "parameters": {},
            "triggers": {},
            "actions": {},
            "outputs": {}
        }
    )
)
```

