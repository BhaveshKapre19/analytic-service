# Database Models

## `Visitor` Model
Stores a single visit from a user to a registered website.

**Fields:**
- `website_name` (CharField)
- `visitor_ip` (GenericIPAddressField)
- Location (Optional CharFields/FloatFields): `country`, `region`, `city`, `latitude`, `longitude`
- Device Info (CharFields/BooleanFields): `browser`, `browser_version`, `operating_system`, `device_type`, `device_brand`, `device_model`, `is_mobile`, `is_tablet`, `is_pc`
- `user_agent` (TextField)
- `language` (CharField)
- `screen_resolution` (CharField, Optional)
- `timezone` (CharField, Optional)
- `referrer` (URLField, Optional)
- `current_page` (CharField)
- `session_id` (CharField)
- `visit_timestamp` (DateTimeField)
- `created_at` (DateTimeField, auto_now_add)
- `updated_at` (DateTimeField, auto_now)
