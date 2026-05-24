test_settings = {
    'theme': 'light',
    'volume': 'high',
    'font_size': 'medium'
}

def add_setting(settings, setting_pair):
    key, value = setting_pair
    key = key.lower()
    value = value.lower()
    
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, setting_pair):
    key, value = setting_pair
    
    key = str(key).lower()
    value = str(value).lower()
    
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    key = str(key).lower()

    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    
    return f"Setting not found!"

def view_settings(settings):
    if not settings:
        return "No settings available."
    
    output = "Current User Settings:"
    
    for key, value in settings.items():
        output += "\n{}: {}".format(str(key).capitalize(), str(value))
        
    return output + "\n"