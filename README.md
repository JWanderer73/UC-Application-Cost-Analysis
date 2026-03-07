# UC-Application-Cost-Analysis

## Description 

Data cleaning, analysis, and visualization code for prediction of total application cost to UC schools over time. The code interprets historical application fee, ap test cost, and average ap test volume data by school to create cleaned datasets. Then, we use regression models to predict up to five years into the future. 

## Local Setup

Clone the repo, then create a datasets folder. For data, we recommend you download the datasets folder from this [Google Drive](https://drive.google.com/drive/folders/1H-ZfhlW7eAbbYQYnVMrslm4a2uzMp23v?usp=drive_link).

If you wish to get the data manually, then for AP exam cost, visit [TotalRegistration's website](https://www.totalregistration.net/AP-Exam-Registration-Service/Follow-The-Money-History-of-College-Board-Finances.php) and download the data.

For UC-specific AP volume data, visit the [UC undergraduate admissions summary](https://www.universityofcalifornia.edu/about-us/information-center/admissions-residency-and-ethnicity) and select (1) all academic years 2003 onward, (2) Systemwide, (3) by honors courses, and (4) All. 

For school application fees, go to the [IPEDS dataset](https://nces.ed.gov/ipeds/datacenter/DataFiles.aspx?year=-1&surveyNumber=-1&sid=42140801-8bc4-4f3b-93ab-151e400fd9b5&rtid=1) and download from:
* [Instituional Characteristics][1] for all years prior to 2024. The correct files are those containing application fees, usually called "student charges."
* [Cost][2] for all years 2024 and further. The application fees file, titled "COST1_2024" is the relevant one.

[1]: https://nces.ed.gov/ipeds/datacenter/DataFiles.aspx?year=-1&surveyNumber=1&sid=42140801-8bc4-4f3b-93ab-151e400fd9b5&rtid=7
[2]: https://nces.ed.gov/ipeds/datacenter/DataFiles.aspx?year=-1&surveyNumber=19&sid=42140801-8bc4-4f3b-93ab-151e400fd9b5&rtid=7

To run the code locally, create a conda forge environment using UCcostenv.yml

## Usage

Each notebook runs independently, and can be run in any order. A brief overview of what is in each notebook is below. For the notebook school_application_fee_prediction.ipynb, first run cleaning_application_fee_historicals.py.

UC_accepted_AP_volume_prediction.ipynb: This notebook works with the the AP Volume data, found [here](https://www.universityofcalifornia.edu/about-us/information-center/admissions-residency-and-ethnicity). This notebook creates plots for the number of AP exams taken at each of the different UCs. Additionally, it creates and tests regression models, which are then used the predict 5 years into the future.

school_application_fee_prediction.ipynb: This notebook works with the UC application fee data found [here](https://nces.ed.gov/ipeds/datacenter/DataFiles.aspx?year=-1&surveyNumber=-1&sid=42140801-8bc4-4f3b-93ab-151e400fd9b5&rtid=1). This notebook creates plots for the cost to apply to UCs over time, and well as the inflation adjusted cost. Additionally, it creates a linear regression model for each school, and uses them to predict 5 years into the future.

AP_test_fee_prediction.ipynb: This notebook works with the AP test fee data found [here](https://www.totalregistration.net/AP-Exam-Registration-Service/Follow-The-Money-History-of-College-Board-Finances.php). This notebook creates a plot for the AP test fees over time, and the inflaiton adjusted fees. Additionally, it creates a linear regression model off it, and uses that to predict the fee cost for the next 5 years.

## Website
To redeploy the website simply fork the repository, and deploy a github pages website from the branch 'website', using the root directory.
