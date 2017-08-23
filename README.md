# Music-Box-Project
Predict users churn for a music box app.
## Dataset
User activity records from 03/01/2017 to 05/12/2017 (many records miss for March 2017)
- play dataset
- download dataset
- search dataset
## Define churn users
0 acticities from 4/22 to 5/12 if users is active(play more than 3 times) from 3/30 to 4/21.
## Downsampling
The whole dataset is too large to handle in personal laptop. So I downsample the data for both active users and churn users.
## Feature creation
- Count by time windows of 3 activities types in different size
- Ratio of the count of different time window
## Train Model
- Logistic regression
- Random Forest
- Gradient Boosted Tree
