from storages.backends.azure_storage import AzureStorage
from azure.storage.blob import generate_blob_sas, BlobSasPermissions
from datetime import datetime, timedelta
from django.conf import settings

class AzureMediaStorage(AzureStorage):
    account_name = settings.AZURE_ACCOUNT_NAME
    account_key = settings.AZURE_ACCOUNT_KEY
    azure_container = settings.AZURE_CONTAINER

    def url(self, name):
        sas_token = generate_blob_sas(
            account_name=self.account_name,
            container_name=self.azure_container,
            blob_name=name,
            account_key=self.account_key,
            permission=BlobSasPermissions(read=True),
            expiry=datetime.utcnow() + timedelta(hours=1)  # URL válida por 1 hora
        )
        return f"https://{self.account_name}.blob.core.windows.net/{self.azure_container}/{name}?{sas_token}"
    
azure_storage = AzureMediaStorage()
