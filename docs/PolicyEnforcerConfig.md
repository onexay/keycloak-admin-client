# policy_enforcer_config.PolicyEnforcerConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enforcement_mode** | [**enforcement_mode.EnforcementMode**](EnforcementMode.md) |  | [optional] 
**paths** | [**[path_config.PathConfig]**](PathConfig.md) |  | [optional] 
**path_cache** | [**path_cache_config.PathCacheConfig**](PathCacheConfig.md) |  | [optional] 
**lazy_load_paths** | **bool** |  | [optional] 
**on_deny_redirect_to** | **str** |  | [optional] 
**user_managed_access** | **bool, date, datetime, dict, float, int, list, str** |  | [optional] 
**claim_information_point** | **{str: ({str: (str,)},)}** |  | [optional] 
**http_method_as_scope** | **bool** |  | [optional] 
**realm** | **str** |  | [optional] 
**auth_server_url** | **str** |  | [optional] 
**credentials** | **{str: (str,)}** |  | [optional] 
**resource** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


