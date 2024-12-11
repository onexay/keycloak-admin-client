# user_representation.UserRepresentation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**email_verified** | **bool** |  | [optional] 
**attributes** | **{str: ([str],)}** |  | [optional] 
**user_profile_metadata** | [**user_profile_metadata.UserProfileMetadata**](UserProfileMetadata.md) |  | [optional] 
**_self** | **str** |  | [optional] 
**origin** | **str** |  | [optional] 
**created_timestamp** | **int** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**totp** | **bool** |  | [optional] 
**federation_link** | **str** |  | [optional] 
**service_account_client_id** | **str** |  | [optional] 
**credentials** | [**[credential_representation.CredentialRepresentation]**](CredentialRepresentation.md) |  | [optional] 
**disableable_credential_types** | **[str]** |  | [optional] 
**required_actions** | **[str]** |  | [optional] 
**federated_identities** | [**[federated_identity_representation.FederatedIdentityRepresentation]**](FederatedIdentityRepresentation.md) |  | [optional] 
**realm_roles** | **[str]** |  | [optional] 
**client_roles** | **{str: ([str],)}** |  | [optional] 
**client_consents** | [**[user_consent_representation.UserConsentRepresentation]**](UserConsentRepresentation.md) |  | [optional] 
**not_before** | **int** |  | [optional] 
**application_roles** | **{str: ([str],)}** |  | [optional] 
**social_links** | [**[social_link_representation.SocialLinkRepresentation]**](SocialLinkRepresentation.md) |  | [optional] 
**groups** | **[str]** |  | [optional] 
**access** | **{str: (bool,)}** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


