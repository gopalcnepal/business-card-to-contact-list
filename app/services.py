import os
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

endpoint = os.getenv('ENDPOINT')
key = os.getenv('KEY')
form_model_id = "prebuilt-businessCard"

def analyze_business_card(business_card_image):
    document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
        )

    poller = document_analysis_client.begin_analyze_document(
        form_model_id, business_card_image
    )
    business_cards = poller.result()

    business_card_data = {}

    for idx, business_card in enumerate(business_cards.documents):
        contact_names = business_card.fields.get("ContactNames")
        if contact_names:
            for contact_name in contact_names.value:
                if contact_name.value["FirstName"].confidence > 0.5 or contact_name.value["LastName"].confidence > 0.5:
                    business_card_data["first_name"] = contact_name.value["FirstName"].value
                    business_card_data["last_name"] = contact_name.value["LastName"].value
                else:
                    business_card_data["first_name"] = ""
                    business_card_data["last_name"] = ""

        company_names = business_card.fields.get("CompanyNames")
        if company_names:
            for company_name in company_names.value:
                if company_name.confidence > 0.5:
                    business_card_data["company"] = company_name.value
                else:
                    business_card_data["company"] = ""

        departments = business_card.fields.get("Departments")
        if departments:
            for department in departments.value:
                if department.confidence > 0.5:
                    business_card_data["department"] = department.value
                else:
                    business_card_data["department"] = ""

        job_titles = business_card.fields.get("JobTitles")
        if job_titles:
            for job_title in job_titles.value:
                if job_title.confidence > 0.5:
                    business_card_data["job_title"] = job_title.value
                else:
                    business_card_data["job_title"] = ""

        emails = business_card.fields.get("Emails")
        if emails:
            for email in emails.value:
                if email.confidence > 0.5:
                    business_card_data["email"] = email.value
                else:
                    business_card_data["email"] = ""

        websites = business_card.fields.get("Websites")
        if websites:
            for website in websites.value:
                if website.confidence > 0.5:
                    business_card_data["website"] = website.value
                else:
                    business_card_data["website"] = ""

        mobile_phones = business_card.fields.get("MobilePhones")
        if mobile_phones:
            for phone in mobile_phones.value:
                if phone.confidence > 0.5:
                    business_card_data["phone"] = phone.value
                else:
                    business_card_data["phone"] = ""
                    
        work_phones = business_card.fields.get("WorkPhones")
        if work_phones:
            for work_phone in work_phones.value:
                if work_phone.confidence > 0.5:
                    business_card_data["work_phone"] = work_phone.value
                else:
                    business_card_data["work_phone"] = ""

    return business_card_data
