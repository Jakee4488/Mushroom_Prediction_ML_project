# GDP_Prediction_ML_project
 ML Python solution to deliver monthly GDP estimates


## Workflows

1. Update config.yaml

2. Update schema.yaml

3. Update params.yaml

4. Update the entity

5. Update the configuration manager in src config

6. Update the components

7. Update the pipeline 

8. Update the main.py

9. Update the app.py




import dagshub
dagshub.init(repo_owner='Jakee4488', repo_name='GDP_Prediction_ML_project', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)