# UC-Application-Cost-Analysis

## Description 

Data cleaning, analysis, and visualization code for prediction of total application cost to UC schools over time. The code interprets historical application fee, ap test cost, and average ap test volume data by school to create cleaned datasets. Then, we use regression models to predict up to five years into the future. 

## Installation

Clone the repo, then create a datasets folder. For data, we recommend you download the datasets folder from this [Google Drive](https://www.google.com).
^Placeholder drive for now.

If you wish to get the data manually, then for AP exam cost, visit [TotalRegistration's website](https://www.totalregistration.net/AP-Exam-Registration-Service/Follow-The-Money-History-of-College-Board-Finances.php) and download the data.

For UC-specific AP volume data, visit the [UC undergraduate admissions summary](https://www.universityofcalifornia.edu/about-us/information-center/admissions-residency-and-ethnicity) and select (1) all academic years 2003 onward, (2) Systemwide, (3) by honors courses, and (4) All. 

For school application fees, go to the [IPEDS dataset](https://nces.ed.gov/ipeds/datacenter/DataFiles.aspx?year=-1&surveyNumber=-1&sid=42140801-8bc4-4f3b-93ab-151e400fd9b5&rtid=1) and download from:
* [Instituional Characteristics][1] for all years prior to 2024. The correct files are those containing application fees, usually called "student charges."
* [Cost][2] for all years 2024 and further. The application fees file, titled "COST1_2024" is the relevant one.

[1]: https://nces.ed.gov/ipeds/datacenter/DataFiles.aspx?year=-1&surveyNumber=1&sid=42140801-8bc4-4f3b-93ab-151e400fd9b5&rtid=7
[2]: https://nces.ed.gov/ipeds/datacenter/DataFiles.aspx?year=-1&surveyNumber=19&sid=42140801-8bc4-4f3b-93ab-151e400fd9b5&rtid=7

## Usage

Run whichever notebook or script you wish. 