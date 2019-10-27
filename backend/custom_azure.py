from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'hackathoninnoai' # Must be replaced by your <storage_account_name>
    account_key = 'IrZ5NR+e/OX4FcHLet9bUdurOX6O6lmRHJRfLn3x4e+hbKQ0tjoCMVi0OxiwHnnzY092cqofXfx4A48AeKfWLw==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'hackathoninnoai' # Must be replaced by your storage_account_name
    account_key = 'IrZ5NR+e/OX4FcHLet9bUdurOX6O6lmRHJRfLn3x4e+hbKQ0tjoCMVi0OxiwHnnzY092cqofXfx4A48AeKfWLw==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None
