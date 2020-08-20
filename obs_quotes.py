# The script is based on url-text.py
 
import random

import obspython as obs

source_file = ""
source_name = ""

def update_text():
    global source_file
    global interval
    global source_name


    source = obs.obs_get_source_by_name(source_name)
    if source is not None:
        try:
            with open(source_file, "r", encoding='utf8') as f:
                lines = f.readlines()
                random_line = random.randint(0, len(lines))
                text = lines[random_line]

                settings = obs.obs_data_create()
                obs.obs_data_set_string(settings, "text", text)
                obs.obs_source_update(source, settings)
                obs.obs_data_release(settings)

        except FileNotFoundError as err:
            if source_file == "":
                error_info = " - no file name was given in the configuration panel"
            else:
                error_info = " - Invalid path or file name \'" + source_file +"\'"
            obs.script_log(obs.LOG_WARNING, "Error opening file " + error_info)
            obs.remove_current_callback()

        obs.obs_source_release(source)

def refresh_pressed(props, prop):
    update_text()


def script_description():

    return '''A plugin that allows you to rotate citations from a file.
Enter a name for the quotation file.
Select the frequency of text changes.
Select the text field to fill with content.'''



def script_update(settings):
    global source_file
    global interval
    global source_name

    source_file = obs.obs_data_get_string(settings, "source_file")
    interval = obs.obs_data_get_int(settings, "interval")
    source_name = obs.obs_data_get_string(settings, "source")

    obs.timer_remove(update_text)

    if source_file != "" and source_name != "":
        obs.timer_add(update_text, interval * 1000)

def script_defaults(settings):
    obs.obs_data_set_default_int(settings, "interval", 10)

def script_properties():
    props = obs.obs_properties_create()

    obs.obs_properties_add_text(props, "source_file", "File with quotes", obs.OBS_TEXT_DEFAULT) #
    obs.obs_properties_add_int(props, "interval", "Quote refresh (seconds)", 10, 3600, 1)

    p = obs.obs_properties_add_list(props, "source", "Text Source", obs.OBS_COMBO_TYPE_EDITABLE, obs.OBS_COMBO_FORMAT_STRING)
    sources = obs.obs_enum_sources()
    if sources is not None:
        for source in sources:
            source_id = obs.obs_source_get_unversioned_id(source)
            if source_id == "text_gdiplus" or source_id == "text_ft2_source":
                name = obs.obs_source_get_name(source)
                obs.obs_property_list_add_string(p, name, name)

        obs.source_list_release(sources)

    obs.obs_properties_add_button(props, "button", "Refresh", refresh_pressed)

    return props

# TODO: dodać file picker i sprawdzić czy da się zawalczyć z domyślną ścieżką do pliku cytatów w katalogu wtyczki
