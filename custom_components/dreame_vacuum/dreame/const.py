from typing import Final
from .types import (
    DreameVacuumChargingStatus,
    DreameVacuumTaskStatus,
    DreameVacuumState,
    DreameVacuumWaterTank,
    DreameVacuumCarpetSensitivity,
    DreameVacuumStatus,
    DreameVacuumErrorCode,
    DreameVacuumRelocationStatus,
    DreameVacuumDustCollection,
    DreameVacuumAutoEmptyStatus,
    DreameVacuumSelfWashBaseStatus,
    DreameVacuumSuctionLevel,
    DreameVacuumWaterVolume,
    DreameVacuumMopPadHumidity,
    DreameVacuumCleaningMode,
    DreameVacuumSelfCleanArea,
    DreameVacuumMopWashLevel,
    DreameVacuumMoppingType,
    DreameVacuumProperty,
    DreameVacuumAction,
)

SUCTION_LEVEL_QUIET: Final = "quiet"
SUCTION_LEVEL_STANDARD: Final = "standard"
SUCTION_LEVEL_STRONG: Final = "strong"
SUCTION_LEVEL_TURBO: Final = "turbo"

WATER_VOLUME_LOW: Final = "low"
WATER_VOLUME_MEDIUM: Final = "medium"
WATER_VOLUME_HIGH: Final = "high"

MOP_PAD_HUMIDITY_SLIGHTLY_DRY: Final = "slightly_dry"
MOP_PAD_HUMIDITY_MOIST: Final = "moist"
MOP_PAD_HUMIDITY_WET: Final = "wet"

CLEANING_MODE_SWEEPING: Final = "sweeping"
CLEANING_MODE_MOPPING: Final = "mopping"
CLEANING_MODE_SWEEPING_AND_MOPPING: Final = "sweeping_and_mopping"

STATE_UNKNOWN: Final = "unknown"
STATE_SWEEPING: Final = "sweeping"
STATE_IDLE: Final = "idle"
STATE_PAUSED: Final = "paused"
STATE_RETURNING: Final = "returning"
STATE_CHARGING: Final = "charging"
STATE_ERROR: Final = "error"
STATE_MOPPING: Final = "mopping"
STATE_DRYING: Final = "drying"
STATE_WASHING: Final = "washing"
STATE_RETURNING_WASHING: Final = "returning_to_washing"
STATE_BUILDING: Final = "building"
STATE_SWEEPING_AND_MOPPING: Final = "sweeping_and_mopping"
STATE_CHARGING_COMPLETED: Final = "charging_completed"
STATE_UPGRADING: Final = "upgrading"
STATE_UNAVAILABLE: Final = "unavailable"

TASK_STATUS_COMPLETED: Final = "completed"
TASK_STATUS_AUTO_CLEANING: Final = "cleaning"
TASK_STATUS_ZONE_CLEANING: Final = "zone_cleaning"
TASK_STATUS_SEGMENT_CLEANING: Final = "room_cleaning"
TASK_STATUS_SPOT_CLEANING: Final = "spot_cleaning"
TASK_STATUS_FAST_MAPPING: Final = "fast_mapping"
TASK_STATUS_AUTO_CLEANING_PAUSE: Final = "cleaning_paused"
TASK_STATUS_SEGMENT_CLEANING_PAUSE: Final = "room_cleaning_paused"
TASK_STATUS_ZONE_CLEANING_PAUSE: Final = "zone_cleaning_paused"
TASK_STATUS_SPOT_CLEANING_PAUSE: Final = "spot_cleaning_paused"
TASK_STATUS_MAP_CLEANING_PAUSE: Final = "map_cleaning_paused"
TASK_STATUS_DOCKING_PAUSE: Final = "docking_paused"
TASK_STATUS_MOPPING_PAUSE: Final = "mopping_paused"
TASK_STATUS_ZONE_MOPPING_PAUSE: Final = "zone_mopping_paused"
TASK_STATUS_SEGMENT_MOPPING_PAUSE: Final = "room_mopping_paused"
TASK_STATUS_AUTO_MOPPING_PAUSE: Final = "mopping_paused"
TASK_STATUS_MONITOR_CRUISE : Final = "monitor_cruise"
TASK_STATUS_MONITOR_CRUISE_PAUSE : Final = "monitor_cruise_pause"
TASK_STATUS_MONITOR_SPOT : Final = "monitor_spot"
TASK_STATUS_MONITOR_SPOT_PAUSE : Final = "monitor_spot_pause"
TASK_STATUS_SUMMON_CLEAN_PAUSE : Final = "summon_clean_pause"
TASK_STATUS_RETURNING_INSTALL_MOP : Final = "returning_to_install_mop"
TASK_STATUS_RETURNING_REMOVE_MOP : Final = "returning_to_remove_mop"

STATUS_CLEANING: Final = "cleaning"
STATUS_FOLLOW_WALL: Final = "follow_wall_cleaning"
STATUS_CHARGING: Final = "charging"
STATUS_OTA: Final = "ota"
STATUS_FCT: Final = "fct"
STATUS_WIFI_SET: Final = "wifi_set"
STATUS_POWER_OFF: Final = "power_off"
STATUS_FACTORY: Final = "factory"
STATUS_ERROR: Final = "error"
STATUS_REMOTE_CONTROL: Final = "remote_control"
STATUS_SLEEP: Final = "sleeping"
STATUS_SELF_TEST: Final = "self_test"
STATUS_FACTORY_FUNC_TEST: Final = "factory_test"
STATUS_STANDBY: Final = "standby"
STATUS_SEGMENT_CLEANING: Final = "room_cleaning"
STATUS_ZONE_CLEANING: Final = "zone_cleaning"
STATUS_SPOT_CLEANING: Final = "spot_cleaning"
STATUS_FAST_MAPPING: Final = "fast_mapping"
STATUS_MONITOR_CRUISE: Final = "monitor_cruise"
STATUS_MONITOR_SPOT: Final = "monitor_spot"
STATUS_SUMMON_CLEAN: Final = "summon_clean"

RELOCATION_STATUS_LOCATED: Final = "located"
RELOCATION_STATUS_LOCATING: Final = "locating"
RELOCATION_STATUS_FAILED: Final = "failed"
RELOCATION_STATUS_SUCESS: Final = "success"

CHARGING_STATUS_CHARGING: Final = "charging"
CHARGING_STATUS_NOT_CHARGING: Final = "not_charging"
CHARGING_STATUS_RETURN_TO_CHARGE: Final = "return_to_charge"
CHARGING_STATUS_CHARGING_COMPLETED: Final = "charging_completed"

DUST_COLLECTION_NOT_AVAILABLE: Final = "not_available"
DUST_COLLECTION_AVAILABLE: Final = "available"

AUTO_EMPTY_STATUS_ACTIVE: Final = "active"
AUTO_EMPTY_STATUS_NOT_PERFORMED: Final = "not_performed"

SELF_WASH_BASE_STATUS_WASHING: Final = "washing"
SELF_WASH_BASE_STATUS_DRYING: Final = "drying"
SELF_WASH_BASE_STATUS_PAUSED: Final = "paused"
SELF_WASH_BASE_STATUS_RETURNING: Final = "returning"
SELF_WASH_BASE_STATUS_CLEAN_ADD_WATER: Final = "clean_add_water"
SELF_WASH_BASE_STATUS_ADDING_WATER: Final = "adding_water"

SELF_AREA_CLEAN_FIVE_SQUARE_METERS: Final = "five_square_meters"
SELF_AREA_CLEAN_TEN_SQUARE_METERS: Final = "ten_square_meters"
SELF_AREA_CLEAN_FIFTEEN_SQUARE_METERS: Final = "fifteen_square_meters"
SELF_AREA_CLEAN_SINGLE_ZONE: Final = "single_zone"

MOP_WASH_LEVEL_DEEP: Final = "deep"
MOP_WASH_LEVEL_DAILY: Final = "daily"
MOP_WASH_LEVEL_WATER_SAVING: Final = "water_saving"

MOPPING_TYPE_DEEP: Final = "deep"
MOPPING_TYPE_DAILY: Final = "daily"
MOPPING_TYPE_ACCURATE: Final = "accurate"

WATER_TANK_INSTALLED: Final = "installed"
WATER_TANK_NOT_INSTALLED: Final = "not_installed"
WATER_TANK_MOP_INSTALLED: Final = "mop_installed"

CARPET_SENSITIVITY_LOW: Final = "low"
CARPET_SENSITIVITY_MEDIUM: Final = "medium"
CARPET_SENSITIVITY_HIGH: Final = "high"

ERROR_NO_ERROR: Final = "no_error"
ERROR_DROP: Final = "drop"
ERROR_CLIFF: Final = "cliff"
ERROR_BUMPER: Final = "bumper"
ERROR_GESTURE: Final = "gesture"
ERROR_BUMPER_REPEAT: Final = "bumper_repeat"
ERROR_DROP_REPEAT: Final = "drop_repeat"
ERROR_OPTICAL_FLOW: Final = "optical_flow"
ERROR_NO_BOX: Final = "no_box"
ERROR_NO_TANKBOX: Final = "no_tank_box"
ERROR_WATERBOX_EMPTY: Final = "water_box_empty"
ERROR_BOX_FULL: Final = "box_full"
ERROR_BRUSH: Final = "brush"
ERROR_SIDE_BRUSH: Final = "side_brush"
ERROR_FAN: Final = "fan"
ERROR_LEFT_WHEEL_MOTOR: Final = "left_wheel_motor"
ERROR_RIGHT_WHEEL_MOTOR: Final = "right_wheel_motor"
ERROR_TURN_SUFFOCATE: Final = "turn_suffocate"
ERROR_FORWARD_SUFFOCATE: Final = "forward_suffocate"
ERROR_CHARGER_GET: Final = "charger_get"
ERROR_BATTERY_LOW: Final = "battery_low"
ERROR_CHARGE_FAULT: Final = "charge_fault"
ERROR_BATTERY_PERCENTAGE: Final = "battery_percentage"
ERROR_HEART: Final = "heart"
ERROR_CAMERA_OCCLUSION: Final = "camera_occlusion"
ERROR_MOVE: Final = "move"
ERROR_FLOW_SHIELDING: Final = "flow_shielding"
ERROR_INFRARED_SHIELDING: Final = "infrared_shielding"
ERROR_CHARGE_NO_ELECTRIC: Final = "charge_no_electric"
ERROR_BATTERY_FAULT: Final = "battery_fault"
ERROR_FAN_SPEED_ERROR: Final = "fan_speed_error"
ERROR_LEFTWHELL_SPEED: Final = "left_wheell_speed"
ERROR_RIGHTWHELL_SPEED: Final = "right_wheell_speed"
ERROR_BMI055_ACCE: Final = "bmi055_acce"
ERROR_BMI055_GYRO: Final = "bmi055_gyro"
ERROR_XV7001: Final = "xv7001"
ERROR_LEFT_MAGNET: Final = "left_magnet"
ERROR_RIGHT_MAGNET: Final = "right_magnet"
ERROR_FLOW_ERROR: Final = "flow_error"
ERROR_INFRARED_FAULT: Final = "infrared_fault"
ERROR_CAMERA_FAULT: Final = "camera_fault"
ERROR_STRONG_MAGNET: Final = "strong_magnet"
ERROR_WATER_PUMP: Final = "water_pump"
ERROR_RTC: Final = "rtc"
ERROR_AUTO_KEY_TRIG: Final = "auto_key_trig"
ERROR_P3V3: Final = "p3v3"
ERROR_CAMERA_IDLE: Final = "camera_idle"
ERROR_BLOCKED: Final = "blocked"
ERROR_LDS_ERROR: Final = "lds_error"
ERROR_LDS_BUMPER: Final = "lds_bumper"
ERROR_FILTER_BLOCKED: Final = "filter_blocked"
ERROR_EDGE: Final = "edge"
ERROR_CARPET: Final = "carpet"
ERROR_LASER: Final = "laser"
ERROR_ULTRASONIC: Final = "ultrasonic"
ERROR_NO_GO_ZONE: Final = "no_go_zone"
ERROR_ROUTE: Final = "route"
ERROR_RESTRICTED: Final = "restricted"
ERROR_REMOVE_MOP: Final = "remove_mop"
ERROR_MOP_REMOVED: Final = "mop_removed"
ERROR_MOP_PAD_STOP_ROTATE: Final = "mop_pad_stop_rotate"
ERROR_BIN_FULL: Final = "bin_full"
ERROR_BIN_OPEN: Final = "bin_open"
ERROR_WATER_TANK: Final = "water_tank"
ERROR_DIRTY_WATER_TANK: Final = "dirty_water_tank"
ERROR_WATER_TANK_DRY: Final = "water_tank_dry"
ERROR_DIRTY_WATER_TANK_BLOCKED: Final = "dirty_water_tank_blocked"
ERROR_DIRTY_WATER_TANK_PUMP: Final = "dirty_water_tank_pump"
ERROR_MOP_PAD: Final = "mop_pad"
ERROR_WET_MOP_PAD: Final = "wet_mop_pad"
ERROR_CLEAN_MOP_PAD: Final = "clean_mop_pad"
ERROR_CLEAN_TANK_LEVEL: Final = "clean_tank_level"
ERROR_DIRTY_TANK_LEVEL: Final = "dirty_tank_level"
ERROR_WASHBOARD_LEVEL: Final = "washboard_level"

ATTR_CHARGING: Final = "charging"
ATTR_STARTED: Final = "started"
ATTR_PAUSED: Final = "paused"
ATTR_RUNNING: Final = "running"
ATTR_RETURNING_PAUSED: Final = "returning_paused"
ATTR_RETURNING: Final = "returning"
ATTR_MAPPING: Final = "mapping"
ATTR_ROOMS: Final = "rooms"
ATTR_CURRENT_SEGMENT: Final = "current_segment"
ATTR_SELECTED_MAP: Final = "selected_map"
ATTR_ID: Final = "id"
ATTR_NAME: Final = "name"
ATTR_ICON: Final = "icon"
ATTR_STATUS: Final = "status"
ATTR_CLEANING_MODE: Final = "cleaning_mode"
ATTR_SUCTION_LEVEL: Final = "suction_level"
ATTR_WATER_TANK: Final = "water_tank"
ATTR_COMPLETED: Final = "completed"
ATTR_CLEANING_TIME: Final = "cleaning_time"
ATTR_CLEANED_AREA: Final = "cleaned_area"
ATTR_MOP_PAD_HUMIDITY: Final = "mop_pad_humidity"
ATTR_MOP_PAD: Final = "mop_pad"
ATTR_CLEANING_SEQUENCE: Final = "cleaning_sequence"

AI_SETTING_SWITCH: Final = "obstacle_detect_switch"
AI_SETTING_UPLOAD: Final = "obstacle_app_display_switch"
AI_SETTING_PET: Final = "whether_have_pet"
AI_SETTING_HUMAN: Final = "human_detect_switch"
AI_SETTING_FURNITURE: Final = "furniture_detect_switch"
AI_SETTING_FLUID: Final = "fluid_detect_switch"

MAP_PARAMETER_NAME: Final = "name"
MAP_PARAMETER_VALUE: Final = "value"
MAP_PARAMETER_TIME: Final = "time"
MAP_PARAMETER_CODE: Final = "code"
MAP_PARAMETER_OUT: Final = "out"
MAP_PARAMETER_MAP: Final = "map"
MAP_PARAMETER_ANGLE: Final = "angle"
MAP_PARAMETER_MAPSTR: Final = "mapstr"
MAP_PARAMETER_CURR_ID: Final = "curr_id"
MAP_PARAMETER_VACUUM: Final = "vacuum"
MAP_PARAMETER_ID: Final = "id"
MAP_PARAMETER_INFO: Final = "info"
MAP_PARAMETER_FIRST: Final = "first"
MAP_PARAMETER_OBJNAME: Final = "objname"
MAP_PARAMETER_RESULT: Final = "result"
MAP_PARAMETER_URL: Final = "url"
MAP_PARAMETER_EXPIRES_TIME: Final = "expires_time"
MAP_PARAMETER_THB: Final = "thb"
MAP_PARAMETER_OBJECT_NAME: Final = "object_name"
MAP_PARAMETER_MD5: Final = "md5"

MAP_REQUEST_PARAMETER_MAP_ID: Final = "map_id"
MAP_REQUEST_PARAMETER_FRAME_ID: Final = "frame_id"
MAP_REQUEST_PARAMETER_FRAME_TYPE: Final = "frame_type"
MAP_REQUEST_PARAMETER_REQ_TYPE: Final = "req_type"
MAP_REQUEST_PARAMETER_FORCE_TYPE: Final = "force_type"
MAP_REQUEST_PARAMETER_TYPE: Final = "type"
MAP_REQUEST_PARAMETER_INDEX: Final = "index"
MAP_REQUEST_PARAMETER_ROOM_ID: Final = "roomID"

MAP_DATA_PARAMETER_CLASS: Final = "__class"
MAP_DATA_PARAMETER_SIZE: Final = "size"
MAP_DATA_PARAMETER_X: Final = "x"
MAP_DATA_PARAMETER_Y: Final = "y"
MAP_DATA_PARAMETER_PIXEL_SIZE: Final = "pixelSize"
MAP_DATA_PARAMETER_LAYERS: Final = "layers"
MAP_DATA_PARAMETER_ENTITIES: Final = "entities"
MAP_DATA_PARAMETER_META_DATA: Final = "metaData"
MAP_DATA_PARAMETER_VERSION: Final = "version"
MAP_DATA_PARAMETER_ROTATION: Final = "rotation"
MAP_DATA_PARAMETER_TYPE: Final = "type"
MAP_DATA_PARAMETER_POINTS: Final = "points"
MAP_DATA_PARAMETER_PIXELS: Final = "pixels"
MAP_DATA_PARAMETER_SEGMENT_ID: Final = "segmentId"
MAP_DATA_PARAMETER_ACTIVE: Final = "active"
MAP_DATA_PARAMETER_NAME: Final = "name"
MAP_DATA_PARAMETER_DIMENSIONS: Final = "dimensions"
MAP_DATA_PARAMETER_MIN: Final = "min"
MAP_DATA_PARAMETER_MAX: Final = "max"
MAP_DATA_PARAMETER_MID: Final = "mid"
MAP_DATA_PARAMETER_AVG: Final = "avg"
MAP_DATA_PARAMETER_PIXEL_COUNT: Final = "pixelCount"
MAP_DATA_PARAMETER_COMPRESSED_PIXELS: Final = "compressedPixels"
MAP_DATA_PARAMETER_ROBOT_POSITION: Final = "robot_position"
MAP_DATA_PARAMETER_CHARGER_POSITION: Final = "charger_location"
MAP_DATA_PARAMETER_NO_MOP_AREA: Final = "no_mop_area"
MAP_DATA_PARAMETER_NO_GO_AREA: Final = "no_go_area"
MAP_DATA_PARAMETER_ACTIVE_ZONE: Final = "active_zone"
MAP_DATA_PARAMETER_VIRTUAL_WALL: Final = "virtual_wall"
MAP_DATA_PARAMETER_PATH: Final = "path"
MAP_DATA_PARAMETER_FLOOR: Final = "floor"
MAP_DATA_PARAMETER_WALL: Final = "wall"
MAP_DATA_PARAMETER_SEGMENT: Final = "segment"

DEVICE_MAP_KEY: Final = "H4sICGt+oGMEAGRldmljZWtleS50eHQAbc67DoIwAIXhd+nsQG8obhaDKFChEg0jBEGJgSIGgsZ3lwbcmL+c/OcDJIKQVGANdN+6u37k2W7/kEshwEIZMZQJfiQS0wQFTly1tjmZpmxVlycjrfMQm1LurvBvctbGXjzfeyKkGQPVlnNrq00trNDPHK6PRMlAneg1mkVucPCErXvFSFBXT0hjtjhA7JVczmzP0GiYDsRFV7KCWg33c8aTcJpBNUvLVAT4vdqYxTbdehX4/gAN9AoFFgEAAA=="

PROPERTY_TO_NAME: Final = {
    DreameVacuumProperty.STATE: ["state", "State"],
    DreameVacuumProperty.ERROR: ["error", "Error"],
    DreameVacuumProperty.BATTERY_LEVEL: ["battery_level", "Battery Level"],
    DreameVacuumProperty.CHARGING_STATUS: ["charging_status", "Charging Status"],
    DreameVacuumProperty.STATUS: ["status", "Status"],
    DreameVacuumProperty.CLEANING_TIME: ["cleaning_time", "Cleaning Time"],
    DreameVacuumProperty.CLEANED_AREA: ["cleaned_area", "Cleaned Area"],
    DreameVacuumProperty.SUCTION_LEVEL: ["suction_level", "Suction Level"],
    DreameVacuumProperty.WATER_VOLUME: ["water_volume", "Water Volume"],
    DreameVacuumProperty.WATER_TANK: ["water_tank", "Water Tank"],
    DreameVacuumProperty.TASK_STATUS: ["task_status", "Task Status"],
    DreameVacuumProperty.RESUME_CLEANING: ["resume_cleaning", "Resume Cleaning"],
    DreameVacuumProperty.CARPET_BOOST: ["carpet_boost", "Carpet Boost"],
    DreameVacuumProperty.REMOTE_CONTROL: ["remote_control", "Remote Control"],
    DreameVacuumProperty.MOP_CLEANING_REMAINDER: [
        "mop_cleaning_remainder",
        "Mop Cleaning Remainder",
    ],
    DreameVacuumProperty.CLEANING_PAUSED: ["cleaning_paused", "Cleaning Paused"],
    DreameVacuumProperty.FAULTS: ["faults", "Faults"],
    DreameVacuumProperty.RELOCATION_STATUS: ["relocation_status", "Relocation Status"],
    DreameVacuumProperty.OBSTACLE_AVOIDANCE: [
        "obstacle_avoidance",
        "Obstacle Avoidance",
    ],
    DreameVacuumProperty.AI_DETECTION: [
        "ai_obstacle_detection",
        "AI Obstacle Detection",
    ],
    DreameVacuumProperty.CLEANING_MODE: ["cleaning_mode", "Cleaning Mode"],
    DreameVacuumProperty.SELF_WASH_BASE_STATUS: [
        "self_wash_base_status",
        "Self-Wash Base Status",
    ],
    DreameVacuumProperty.CUSTOMIZED_CLEANING: [
        "customized_cleaning",
        "Customized Cleaning",
    ],
    DreameVacuumProperty.CHILD_LOCK: ["child_lock", "Child Lock"],
    DreameVacuumProperty.CARPET_SENSITIVITY: [
        "carpet_sensitivity",
        "Carpet Sensitivity",
    ],
    DreameVacuumProperty.TIGHT_MOPPING: ["tight_mopping", "Tight Mopping"],
    DreameVacuumProperty.CLEANING_CANCEL: ["cleaning_cancel", "Cleaning Cancel"],
    DreameVacuumProperty.CARPET_RECOGNITION: [
        "carpet_recognition",
        "Carpet Recognition",
    ],
    DreameVacuumProperty.SELF_CLEAN: ["self_clean", "Self-Clean"],
    DreameVacuumProperty.WARN_STATUS: ["warn_status", "Warn Status"],
    DreameVacuumProperty.CARPET_AVOIDANCE: ["carpet_avoidance", "Carpet Avoidance"],
    DreameVacuumProperty.AUTO_ADD_DETERGENT: [
        "auto_add_detergent",
        "Auto-Add Detergent",
    ],
    DreameVacuumProperty.DRYING_TIME: ["drying_time", "Drying Time"],
    DreameVacuumProperty.DND: ["dnd", "DnD"],
    DreameVacuumProperty.DND_START: ["dnd_start", "DnD Start"],
    DreameVacuumProperty.DND_END: ["dnd_end", "DnD End"],
    DreameVacuumProperty.MULTI_FLOOR_MAP: ["multi_floor_map", "Multi Floor Map"],
    DreameVacuumProperty.MAP_LIST: ["map_list", "Map List"],
    DreameVacuumProperty.RECOVERY_MAP_LIST: ["recovery_map_list", "Recovery Map List"],
    DreameVacuumProperty.MAP_RECOVERY: ["map_recovery", "Map Recovery"],
    DreameVacuumProperty.MAP_RECOVERY_STATUS: [
        "map_recovery_status",
        "Map Recovery Status",
    ],
    DreameVacuumProperty.VOLUME: ["volume", "Volume"],
    DreameVacuumProperty.SCHEDULE: ["schedule", "Schedule"],
    DreameVacuumProperty.AUTO_DUST_COLLECTING: [
        "auto_dust_collecting",
        "Auto Dust Collecting",
    ],
    DreameVacuumProperty.AUTO_EMPTY_FREQUENCY: [
        "auto_empty_frequency",
        "Auto Empty Frequency",
    ],
    DreameVacuumProperty.MAP_SAVING: [
        "map_saving",
        "Map Saving",
    ],
    DreameVacuumProperty.DUST_COLLECTION: ["dust_collection", "Dust Collection"],
    DreameVacuumProperty.AUTO_EMPTY_STATUS: ["auto_empty_status", "Auto Empty Status"],
    DreameVacuumProperty.SERIAL_NUMBER: ["serial_number", "Serial Number"],
    DreameVacuumProperty.VOICE_PACKET_ID: ["voice_packet_id", "Voice Packet Id"],
    DreameVacuumProperty.TIMEZONE: ["timezone", "Timezone"],
    DreameVacuumProperty.MAIN_BRUSH_TIME_LEFT: [
        "main_brush_time_left",
        "Main Brush  Time Left",
    ],
    DreameVacuumProperty.MAIN_BRUSH_LEFT: ["main_brush_left", "Main Brush Left"],
    DreameVacuumProperty.SIDE_BRUSH_TIME_LEFT: [
        "side_brush_time_left",
        "Side Brush Time Left",
    ],
    DreameVacuumProperty.SIDE_BRUSH_LEFT: ["side_brush_left", "Side Brush Left"],
    DreameVacuumProperty.FILTER_LEFT: ["filter_left", "Filter Left"],
    DreameVacuumProperty.FILTER_TIME_LEFT: ["filter_time_left", "Filter Time Left"],
    DreameVacuumProperty.FIRST_CLEANING_DATE: [
        "first_cleaning_date",
        "First Cleaning Date",
    ],
    DreameVacuumProperty.TOTAL_CLEANING_TIME: [
        "total_cleaning_time",
        "Total Cleaning Time",
    ],
    DreameVacuumProperty.CLEANING_COUNT: ["cleaning_count", "Cleaning Count"],
    DreameVacuumProperty.TOTAL_CLEANED_AREA: [
        "total_cleaned_area",
        "Total Cleaned Area",
    ],
    DreameVacuumProperty.SENSOR_DIRTY_LEFT: ["sensor_dirty_left", "Sensor Dirty Left"],
    DreameVacuumProperty.SENSOR_DIRTY_TIME_LEFT: [
        "sensor_dirty_time_left",
        "Sensor Dirty Time Left",
    ],
    DreameVacuumProperty.SECONDARY_FILTER_LEFT: ["secondary_filter_left", "Secondary Filter Left"],
    DreameVacuumProperty.SECONDARY_FILTER_TIME_LEFT: ["secondary_filter_time_left", "Secondary Filter Time Left"],
    DreameVacuumProperty.MOP_PAD_LEFT: ["mop_pad_left", "Mop Pad Left"],
    DreameVacuumProperty.MOP_PAD_TIME_LEFT: ["mop_pad_time_left", "Mop Pad Time Left"],
    DreameVacuumProperty.SILVER_ION_LEFT: ["silver_ion_left", "Silver-ion Left"],
    DreameVacuumProperty.SILVER_ION_TIME_LEFT: ["silver_ion_time_left", "Silver-ion Time Left"],
    DreameVacuumProperty.DETERGENT_LEFT: ["detergent_left", "Detergent Left"],
    DreameVacuumProperty.DETERGENT_TIME_LEFT: ["detergent_time_left", "Detergent Time Left"],
}

ACTION_TO_NAME: Final = {
    DreameVacuumAction.START: ["start", "Start"],
    DreameVacuumAction.PAUSE: ["pause", "Pause"],
    DreameVacuumAction.CHARGE: ["charge", "Charge"],
    DreameVacuumAction.START_CUSTOM: ["start_custom", "Start Custom"],
    DreameVacuumAction.STOP: ["stop", "Stop"],
    DreameVacuumAction.CLEAR_WARNING: ["clear_warning", "Clear Warning"],
    DreameVacuumAction.REQUEST_MAP: ["request_map", "Request Map"],
    DreameVacuumAction.UPDATE_MAP_DATA: ["update_map_data", "Update Map Data"],
    DreameVacuumAction.LOCATE: ["locate", "Locate"],
    DreameVacuumAction.TEST_SOUND: ["test_sound", "Test Sound"],
    DreameVacuumAction.RESET_MAIN_BRUSH: ["reset_main_brush", "Reset Main Brush"],
    DreameVacuumAction.RESET_SIDE_BRUSH: ["reset_side_brush", "Reset Side Brush"],
    DreameVacuumAction.RESET_FILTER: ["reset_filter", "Reset Filter"],
    DreameVacuumAction.RESET_SENSOR: ["reset_sensor", "Reset Sensor"],
    DreameVacuumAction.START_AUTO_EMPTY: ["start_auto_empty", "Start Auto Empty"],
    DreameVacuumAction.RESET_MOP_PAD: ["reset_mop_pad", "Reset Mop Pad"],
    DreameVacuumAction.RESET_SILVER_ION: ["reset_silver_ion", "Reset Silver-ion"],
    DreameVacuumAction.RESET_DETERGENT: ["reset_detergent", "Reset Detergent"],
}

STATE_CODE_TO_STATE: Final = {
    DreameVacuumState.UNKNOWN: STATE_UNKNOWN,
    DreameVacuumState.SWEEPING: STATE_SWEEPING,
    DreameVacuumState.IDLE: STATE_IDLE,
    DreameVacuumState.PAUSED: STATE_PAUSED,
    DreameVacuumState.ERROR: STATE_ERROR,
    DreameVacuumState.RETURNING: STATE_RETURNING,
    DreameVacuumState.CHARGING: STATE_CHARGING,
    DreameVacuumState.MOPPING: STATE_MOPPING,
    DreameVacuumState.DRYING: STATE_DRYING,
    DreameVacuumState.WASHING: STATE_WASHING,
    DreameVacuumState.RETURNING_WASHING: STATE_RETURNING_WASHING,
    DreameVacuumState.BUILDING: STATE_BUILDING,
    DreameVacuumState.SWEEPING_AND_MOPPING: STATE_SWEEPING_AND_MOPPING,
    DreameVacuumState.CHARGING_COMPLETED: STATE_CHARGING_COMPLETED,
    DreameVacuumState.UPGRADING: STATE_UPGRADING,
}

# Dreame Vacuum suction level names
SUCTION_LEVEL_CODE_TO_NAME: Final = {
    DreameVacuumSuctionLevel.QUIET: SUCTION_LEVEL_QUIET,
    DreameVacuumSuctionLevel.STANDARD: SUCTION_LEVEL_STANDARD,
    DreameVacuumSuctionLevel.STRONG: SUCTION_LEVEL_STRONG,
    DreameVacuumSuctionLevel.TURBO: SUCTION_LEVEL_TURBO,
}

# Dreame Vacuum water volume names
WATER_VOLUME_CODE_TO_NAME: Final = {
    DreameVacuumWaterVolume.LOW: WATER_VOLUME_LOW,
    DreameVacuumWaterVolume.MEDIUM: WATER_VOLUME_MEDIUM,
    DreameVacuumWaterVolume.HIGH: WATER_VOLUME_HIGH,
}

# Dreame Vacuum mop pad humidity names
MOP_PAD_HUMIDITY_CODE_TO_NAME: Final = {
    DreameVacuumMopPadHumidity.SLIGHTLY_DRY: MOP_PAD_HUMIDITY_SLIGHTLY_DRY,
    DreameVacuumMopPadHumidity.MOIST: MOP_PAD_HUMIDITY_MOIST,
    DreameVacuumMopPadHumidity.WET: MOP_PAD_HUMIDITY_WET,
}

# Dreame Vacuum cleaning mode names
CLEANING_MODE_CODE_TO_NAME: Final = {
    DreameVacuumCleaningMode.SWEEPING: CLEANING_MODE_SWEEPING,
    DreameVacuumCleaningMode.MOPPING: CLEANING_MODE_MOPPING,
    DreameVacuumCleaningMode.SWEEPING_AND_MOPPING: CLEANING_MODE_SWEEPING_AND_MOPPING,
}

WATER_TANK_CODE_TO_NAME: Final = {
    DreameVacuumWaterTank.INSTALLED: WATER_TANK_INSTALLED,
    DreameVacuumWaterTank.NOT_INSTALLED: WATER_TANK_NOT_INSTALLED,
    DreameVacuumWaterTank.MOP_INSTALLED: WATER_TANK_MOP_INSTALLED,
}

CARPET_SENSITIVITY_CODE_TO_NAME: Final = {
    DreameVacuumCarpetSensitivity.LOW: CARPET_SENSITIVITY_LOW,
    DreameVacuumCarpetSensitivity.MEDIUM: CARPET_SENSITIVITY_MEDIUM,
    DreameVacuumCarpetSensitivity.HIGH: CARPET_SENSITIVITY_HIGH,
}

TASK_STATUS_CODE_TO_NAME: Final = {
    DreameVacuumTaskStatus.COMPLETED: TASK_STATUS_COMPLETED,
    DreameVacuumTaskStatus.AUTO_CLEANING: TASK_STATUS_AUTO_CLEANING,
    DreameVacuumTaskStatus.ZONE_CLEANING: TASK_STATUS_ZONE_CLEANING,
    DreameVacuumTaskStatus.SEGMENT_CLEANING: TASK_STATUS_SEGMENT_CLEANING,
    DreameVacuumTaskStatus.SPOT_CLEANING: TASK_STATUS_SPOT_CLEANING,
    DreameVacuumTaskStatus.FAST_MAPPING: TASK_STATUS_FAST_MAPPING,
    DreameVacuumTaskStatus.AUTO_CLEANING_PAUSED: TASK_STATUS_AUTO_CLEANING_PAUSE,
    DreameVacuumTaskStatus.SEGMENT_CLEANING_PAUSED: TASK_STATUS_SEGMENT_CLEANING_PAUSE,
    DreameVacuumTaskStatus.ZONE_CLEANING_PAUSED: TASK_STATUS_ZONE_CLEANING_PAUSE,
    DreameVacuumTaskStatus.SPOT_CLEANING_PAUSED: TASK_STATUS_SPOT_CLEANING_PAUSE,
    DreameVacuumTaskStatus.MAP_CLEANING_PAUSED: TASK_STATUS_MAP_CLEANING_PAUSE,
    DreameVacuumTaskStatus.DOCKING_PAUSED: TASK_STATUS_DOCKING_PAUSE,
    DreameVacuumTaskStatus.MOPPING_PAUSED: TASK_STATUS_MOPPING_PAUSE,
    DreameVacuumTaskStatus.ZONE_MOPPING_PAUSED: TASK_STATUS_ZONE_MOPPING_PAUSE,
    DreameVacuumTaskStatus.SEGMENT_MOPPING_PAUSED: TASK_STATUS_SEGMENT_MOPPING_PAUSE,
    DreameVacuumTaskStatus.AUTO_MOPPING_PAUSED: TASK_STATUS_AUTO_MOPPING_PAUSE,
    DreameVacuumTaskStatus.AUTO_DOCKING_PAUSED: TASK_STATUS_DOCKING_PAUSE,
    DreameVacuumTaskStatus.ZONE_DOCKING_PAUSED: TASK_STATUS_DOCKING_PAUSE,
    DreameVacuumTaskStatus.SEGMENT_DOCKING_PAUSED: TASK_STATUS_DOCKING_PAUSE,
    DreameVacuumTaskStatus.MONITOR_CRUISE: TASK_STATUS_MONITOR_CRUISE,
    DreameVacuumTaskStatus.MONITOR_CRUISE_PAUSE: TASK_STATUS_MONITOR_CRUISE_PAUSE,
    DreameVacuumTaskStatus.MONITOR_SPOT: TASK_STATUS_MONITOR_SPOT,
    DreameVacuumTaskStatus.MONITOR_SPOT_PAUSE: TASK_STATUS_MONITOR_SPOT_PAUSE,
    DreameVacuumTaskStatus.SUMMON_CLEAN_PAUSE: TASK_STATUS_SUMMON_CLEAN_PAUSE,
    DreameVacuumTaskStatus.RETURNING_INSTALL_MOP: TASK_STATUS_RETURNING_INSTALL_MOP,
    DreameVacuumTaskStatus.RETURNING_REMOVE_MOP: TASK_STATUS_RETURNING_REMOVE_MOP,
}

STATUS_CODE_TO_NAME: Final = {
    DreameVacuumStatus.IDLE: STATE_IDLE,
    DreameVacuumStatus.PAUSED: STATE_PAUSED,
    DreameVacuumStatus.CLEANING: STATUS_CLEANING,
    DreameVacuumStatus.BACK_HOME: STATE_RETURNING,
    DreameVacuumStatus.PART_CLEANING: STATUS_SPOT_CLEANING,
    DreameVacuumStatus.FOLLOW_WALL: STATUS_FOLLOW_WALL,
    DreameVacuumStatus.CHARGING: STATUS_CHARGING,
    DreameVacuumStatus.OTA: STATUS_OTA,
    DreameVacuumStatus.FCT: STATUS_FCT,
    DreameVacuumStatus.WIFI_SET: STATUS_WIFI_SET,
    DreameVacuumStatus.POWER_OFF: STATUS_POWER_OFF,
    DreameVacuumStatus.FACTORY: STATUS_FACTORY,
    DreameVacuumStatus.ERROR: STATUS_ERROR,
    DreameVacuumStatus.REMOTE_CONTROL: STATUS_REMOTE_CONTROL,
    DreameVacuumStatus.SLEEPING: STATUS_SLEEP,
    DreameVacuumStatus.SELF_TEST: STATUS_SELF_TEST,
    DreameVacuumStatus.FACTORY_FUNCION_TEST: STATUS_FACTORY_FUNC_TEST,
    DreameVacuumStatus.STANDBY: STATUS_STANDBY,
    DreameVacuumStatus.SEGMENT_CLEANING: STATUS_SEGMENT_CLEANING,
    DreameVacuumStatus.ZONE_CLEANING: STATUS_ZONE_CLEANING,
    DreameVacuumStatus.SPOT_CLEANING: STATUS_SPOT_CLEANING,
    DreameVacuumStatus.FAST_MAPPING: STATUS_FAST_MAPPING,
    DreameVacuumStatus.MONITOR_CRUISE: STATUS_MONITOR_CRUISE,
    DreameVacuumStatus.MONITOR_SPOT: STATUS_MONITOR_SPOT,
    DreameVacuumStatus.SUMMON_CLEAN: STATUS_SUMMON_CLEAN,
}

RELOCATION_STATUS_CODE_TO_NAME: Final = {
    DreameVacuumRelocationStatus.LOCATED: RELOCATION_STATUS_LOCATED,
    DreameVacuumRelocationStatus.LOCATING: RELOCATION_STATUS_LOCATING,
    DreameVacuumRelocationStatus.FAILED: RELOCATION_STATUS_FAILED,
    DreameVacuumRelocationStatus.SUCCESS: RELOCATION_STATUS_SUCESS,
}

CHARGING_STATUS_CODE_TO_NAME: Final = {
    DreameVacuumChargingStatus.CHARGING: CHARGING_STATUS_CHARGING,
    DreameVacuumChargingStatus.NOT_CHARGING: CHARGING_STATUS_NOT_CHARGING,
    DreameVacuumChargingStatus.CHARGING_COMPLETED: CHARGING_STATUS_CHARGING_COMPLETED,
    DreameVacuumChargingStatus.RETURN_TO_CHARGE: CHARGING_STATUS_RETURN_TO_CHARGE,
}

ERROR_CODE_TO_ERROR_NAME: Final = {
    DreameVacuumErrorCode.NO_ERROR: ERROR_NO_ERROR,
    DreameVacuumErrorCode.DROP: ERROR_DROP,
    DreameVacuumErrorCode.CLIFF: ERROR_CLIFF,
    DreameVacuumErrorCode.BUMPER: ERROR_BUMPER,
    DreameVacuumErrorCode.GESTURE: ERROR_GESTURE,
    DreameVacuumErrorCode.BUMPER_REPEAT: ERROR_BUMPER_REPEAT,
    DreameVacuumErrorCode.DROP_REPEAT: ERROR_DROP_REPEAT,
    DreameVacuumErrorCode.OPTICAL_FLOW: ERROR_OPTICAL_FLOW,
    DreameVacuumErrorCode.BOX: ERROR_NO_BOX,
    DreameVacuumErrorCode.TANKBOX: ERROR_NO_TANKBOX,
    DreameVacuumErrorCode.WATERBOX_EMPTY: ERROR_WATERBOX_EMPTY,
    DreameVacuumErrorCode.BOX_FULL: ERROR_BOX_FULL,
    DreameVacuumErrorCode.BRUSH: ERROR_BRUSH,
    DreameVacuumErrorCode.SIDE_BRUSH: ERROR_SIDE_BRUSH,
    DreameVacuumErrorCode.FAN: ERROR_FAN,
    DreameVacuumErrorCode.LEFT_WHEEL_MOTOR: ERROR_LEFT_WHEEL_MOTOR,
    DreameVacuumErrorCode.RIGHT_WHEEL_MOTOR: ERROR_RIGHT_WHEEL_MOTOR,
    DreameVacuumErrorCode.TURN_SUFFOCATE: ERROR_TURN_SUFFOCATE,
    DreameVacuumErrorCode.FORWARD_SUFFOCATE: ERROR_FORWARD_SUFFOCATE,
    DreameVacuumErrorCode.CHARGER_GET: ERROR_CHARGER_GET,
    DreameVacuumErrorCode.BATTERY_LOW: ERROR_BATTERY_LOW,
    DreameVacuumErrorCode.CHARGE_FAULT: ERROR_CHARGE_FAULT,
    DreameVacuumErrorCode.BATTERY_PERCENTAGE: ERROR_BATTERY_PERCENTAGE,
    DreameVacuumErrorCode.HEART: ERROR_HEART,
    DreameVacuumErrorCode.CAMERA_OCCLUSION: ERROR_CAMERA_OCCLUSION,
    DreameVacuumErrorCode.MOVE: ERROR_MOVE,
    DreameVacuumErrorCode.FLOW_SHIELDING: ERROR_FLOW_SHIELDING,
    DreameVacuumErrorCode.INFRARED_SHIELDING: ERROR_INFRARED_SHIELDING,
    DreameVacuumErrorCode.CHARGE_NO_ELECTRIC: ERROR_CHARGE_NO_ELECTRIC,
    DreameVacuumErrorCode.BATTERY_FAULT: ERROR_BATTERY_FAULT,
    DreameVacuumErrorCode.FAN_SPEED_ERROR: ERROR_FAN_SPEED_ERROR,
    DreameVacuumErrorCode.LEFTWHELL_SPEED: ERROR_LEFTWHELL_SPEED,
    DreameVacuumErrorCode.RIGHTWHELL_SPEED: ERROR_RIGHTWHELL_SPEED,
    DreameVacuumErrorCode.BMI055_ACCE: ERROR_BMI055_ACCE,
    DreameVacuumErrorCode.BMI055_GYRO: ERROR_BMI055_GYRO,
    DreameVacuumErrorCode.XV7001: ERROR_XV7001,
    DreameVacuumErrorCode.LEFT_MAGNET: ERROR_LEFT_MAGNET,
    DreameVacuumErrorCode.RIGHT_MAGNET: ERROR_RIGHT_MAGNET,
    DreameVacuumErrorCode.FLOW_ERROR: ERROR_FLOW_ERROR,
    DreameVacuumErrorCode.INFRARED_FAULT: ERROR_INFRARED_FAULT,
    DreameVacuumErrorCode.CAMERA_FAULT: ERROR_CAMERA_FAULT,
    DreameVacuumErrorCode.STRONG_MAGNET: ERROR_STRONG_MAGNET,
    DreameVacuumErrorCode.WATER_PUMP: ERROR_WATER_PUMP,
    DreameVacuumErrorCode.RTC: ERROR_RTC,
    DreameVacuumErrorCode.AUTO_KEY_TRIG: ERROR_AUTO_KEY_TRIG,
    DreameVacuumErrorCode.P3V3: ERROR_P3V3,
    DreameVacuumErrorCode.CAMERA_IDLE: ERROR_CAMERA_IDLE,
    DreameVacuumErrorCode.BLOCKED: ERROR_BLOCKED,
    DreameVacuumErrorCode.LDS_ERROR: ERROR_LDS_ERROR,
    DreameVacuumErrorCode.LDS_BUMPER: ERROR_LDS_BUMPER,
    DreameVacuumErrorCode.WATER_PUMP_2: ERROR_WATER_PUMP,
    DreameVacuumErrorCode.FILTER_BLOCKED: ERROR_FILTER_BLOCKED,
    DreameVacuumErrorCode.EDGE: ERROR_EDGE,
    DreameVacuumErrorCode.CARPET: ERROR_CARPET,
    DreameVacuumErrorCode.LASER: ERROR_LASER,
    DreameVacuumErrorCode.EDGE_2: ERROR_EDGE,
    DreameVacuumErrorCode.ULTRASONIC: ERROR_ULTRASONIC,
    DreameVacuumErrorCode.NO_GO_ZONE: ERROR_NO_GO_ZONE,
    DreameVacuumErrorCode.ROUTE: ERROR_ROUTE,
    DreameVacuumErrorCode.ROUTE_2: ERROR_ROUTE,
    DreameVacuumErrorCode.BLOCKED_2: ERROR_BLOCKED,
    DreameVacuumErrorCode.BLOCKED_3: ERROR_BLOCKED,
    DreameVacuumErrorCode.RESTRICTED: ERROR_RESTRICTED,
    DreameVacuumErrorCode.RESTRICTED_2: ERROR_RESTRICTED,
    DreameVacuumErrorCode.RESTRICTED_3: ERROR_RESTRICTED,
    DreameVacuumErrorCode.REMOVE_MOP: ERROR_REMOVE_MOP,
    DreameVacuumErrorCode.MOP_REMOVED: ERROR_MOP_REMOVED,
    DreameVacuumErrorCode.MOP_REMOVED_2: ERROR_MOP_REMOVED,
    DreameVacuumErrorCode.MOP_PAD_STOP_ROTATE: ERROR_MOP_PAD_STOP_ROTATE,
    DreameVacuumErrorCode.MOP_PAD_STOP_ROTATE_2: ERROR_MOP_PAD_STOP_ROTATE,
    DreameVacuumErrorCode.BIN_FULL: ERROR_BIN_FULL,
    DreameVacuumErrorCode.BIN_OPEN: ERROR_BIN_OPEN,
    DreameVacuumErrorCode.BIN_OPEN_2: ERROR_BIN_OPEN,
    DreameVacuumErrorCode.WATER_TANK: ERROR_WATER_TANK,
    DreameVacuumErrorCode.DIRTY_WATER_TANK: ERROR_DIRTY_WATER_TANK,
    DreameVacuumErrorCode.WATER_TANK_DRY: ERROR_WATER_TANK_DRY,
    DreameVacuumErrorCode.DIRTY_WATER_TANK_2: ERROR_DIRTY_WATER_TANK,
    DreameVacuumErrorCode.DIRTY_WATER_TANK_BLOCKED: ERROR_DIRTY_WATER_TANK_BLOCKED,
    DreameVacuumErrorCode.DIRTY_WATER_TANK_PUMP: ERROR_DIRTY_WATER_TANK_PUMP,
    DreameVacuumErrorCode.MOP_PAD: ERROR_MOP_PAD,
    DreameVacuumErrorCode.WET_MOP_PAD: ERROR_WET_MOP_PAD,
    DreameVacuumErrorCode.CLEAN_MOP_PAD: ERROR_CLEAN_MOP_PAD,
    DreameVacuumErrorCode.CLEAN_TANK_LEVEL: ERROR_CLEAN_TANK_LEVEL,
    DreameVacuumErrorCode.DIRTY_TANK_LEVEL: ERROR_DIRTY_TANK_LEVEL,
    DreameVacuumErrorCode.WASHBOARD_LEVEL: ERROR_WASHBOARD_LEVEL,
}

DUST_COLLECTION_TO_NAME: Final = {
    DreameVacuumDustCollection.NOT_AVAILABLE: DUST_COLLECTION_NOT_AVAILABLE,
    DreameVacuumDustCollection.AVAILABLE: DUST_COLLECTION_AVAILABLE,
}

AUTO_EMPTY_STATUS_TO_NAME: Final = {
    DreameVacuumAutoEmptyStatus.IDLE: STATE_IDLE,
    DreameVacuumAutoEmptyStatus.ACTIVE: AUTO_EMPTY_STATUS_ACTIVE,
    DreameVacuumAutoEmptyStatus.NOT_PERFORMED: AUTO_EMPTY_STATUS_NOT_PERFORMED,
}

SELF_WASH_BASE_STATUS_TO_NAME: Final = {
    DreameVacuumSelfWashBaseStatus.IDLE: STATE_IDLE,
    DreameVacuumSelfWashBaseStatus.WASHING: SELF_WASH_BASE_STATUS_WASHING,
    DreameVacuumSelfWashBaseStatus.DRYING: SELF_WASH_BASE_STATUS_DRYING,
    DreameVacuumSelfWashBaseStatus.PAUSED: SELF_WASH_BASE_STATUS_PAUSED,
    DreameVacuumSelfWashBaseStatus.RETURNING: SELF_WASH_BASE_STATUS_RETURNING,
    DreameVacuumSelfWashBaseStatus.CLEAN_ADD_WATER: SELF_WASH_BASE_STATUS_CLEAN_ADD_WATER,
    DreameVacuumSelfWashBaseStatus.ADDING_WATER: SELF_WASH_BASE_STATUS_ADDING_WATER,
}

SELF_AREA_CLEAN_TO_NAME: Final = {
    DreameVacuumSelfCleanArea.FIVE_SQUARE_METERS: SELF_AREA_CLEAN_FIVE_SQUARE_METERS,
    DreameVacuumSelfCleanArea.TEN_SQUARE_METERS: SELF_AREA_CLEAN_TEN_SQUARE_METERS,
    DreameVacuumSelfCleanArea.FIFTEEN_SQUARE_METERS: SELF_AREA_CLEAN_FIFTEEN_SQUARE_METERS,
    DreameVacuumSelfCleanArea.SINGLE_ZONE: SELF_AREA_CLEAN_SINGLE_ZONE,
}

MOP_WASH_LEVEL_TO_NAME: Final = {
    DreameVacuumMopWashLevel.DEEP: MOP_WASH_LEVEL_DEEP,
    DreameVacuumMopWashLevel.DAILY: MOP_WASH_LEVEL_DAILY,
    DreameVacuumMopWashLevel.WATER_SAVING: MOP_WASH_LEVEL_WATER_SAVING,
}

MOPPING_TYPE_TO_NAME: Final = {
    DreameVacuumMoppingType.DEEP: MOPPING_TYPE_DEEP,
    DreameVacuumMoppingType.DAILY: MOPPING_TYPE_DAILY,
    DreameVacuumMoppingType.ACCURATE: MOPPING_TYPE_ACCURATE,
}

ERROR_CODE_TO_IMAGE_INDEX: Final = {
    DreameVacuumErrorCode.BUMPER: 1,
    DreameVacuumErrorCode.BUMPER_REPEAT: 1,
    DreameVacuumErrorCode.DROP: 2,
    DreameVacuumErrorCode.DROP_REPEAT: 2,
    DreameVacuumErrorCode.CLIFF: 3,
    DreameVacuumErrorCode.GESTURE: 15,
    DreameVacuumErrorCode.BRUSH: 4,
    DreameVacuumErrorCode.SIDE_BRUSH: 5,
    DreameVacuumErrorCode.LEFT_WHEEL_MOTOR: 6,
    DreameVacuumErrorCode.RIGHT_WHEEL_MOTOR: 6,
    DreameVacuumErrorCode.LEFTWHELL_SPEED: 6,
    DreameVacuumErrorCode.RIGHTWHELL_SPEED: 6,
    DreameVacuumErrorCode.TURN_SUFFOCATE: 7,
    DreameVacuumErrorCode.FORWARD_SUFFOCATE: 7,
    DreameVacuumErrorCode.BOX: 8,
    DreameVacuumErrorCode.BOX_FULL: 9,
    DreameVacuumErrorCode.FAN: 9,
    DreameVacuumErrorCode.FILTER_BLOCKED: 9,
    DreameVacuumErrorCode.CHARGE_FAULT: 12,
    DreameVacuumErrorCode.CHARGE_NO_ELECTRIC: 16,
    DreameVacuumErrorCode.BATTERY_FAULT: 29,
    DreameVacuumErrorCode.INFRARED_FAULT: 39,
    DreameVacuumErrorCode.LDS_ERROR: 48,
    DreameVacuumErrorCode.LDS_BUMPER: 49,
    DreameVacuumErrorCode.EDGE: 54,
    DreameVacuumErrorCode.EDGE_2: 54,
    DreameVacuumErrorCode.CARPET: 55,
    DreameVacuumErrorCode.ULTRASONIC: 58,
    DreameVacuumErrorCode.ROUTE: 61,
    DreameVacuumErrorCode.ROUTE_2: 62,
    DreameVacuumErrorCode.BLOCKED: 63,
    DreameVacuumErrorCode.BLOCKED_2: 63,
    DreameVacuumErrorCode.BLOCKED_3: 64,
    DreameVacuumErrorCode.RESTRICTED: 65,
    DreameVacuumErrorCode.RESTRICTED_2: 65,
    DreameVacuumErrorCode.RESTRICTED_3: 65,
    DreameVacuumErrorCode.MOP_REMOVED: 69,
    DreameVacuumErrorCode.MOP_PAD_STOP_ROTATE: 69,
    DreameVacuumErrorCode.MOP_PAD_STOP_ROTATE_2: 69,
    DreameVacuumErrorCode.BIN_FULL: 101,
    DreameVacuumErrorCode.BIN_FULL_2: 101,
    DreameVacuumErrorCode.BIN_OPEN: 102,
    DreameVacuumErrorCode.BIN_OPEN_2: 102,
    DreameVacuumErrorCode.WATER_TANK: 105,
    DreameVacuumErrorCode.CLEAN_TANK_LEVEL: 105,
    DreameVacuumErrorCode.DIRTY_WATER_TANK: 106,
    DreameVacuumErrorCode.DIRTY_WATER_TANK_2: 106,
    DreameVacuumErrorCode.DIRTY_WATER_TANK_BLOCKED: 106,
    DreameVacuumErrorCode.DIRTY_WATER_TANK_PUMP: 106,
    DreameVacuumErrorCode.DIRTY_TANK_LEVEL: 106,
    DreameVacuumErrorCode.WATER_TANK_DRY: 107,
    DreameVacuumErrorCode.MOP_PAD: 111,
    DreameVacuumErrorCode.WET_MOP_PAD: 111,
    DreameVacuumErrorCode.WASHBOARD_LEVEL: 111,
    DreameVacuumErrorCode.CLEAN_MOP_PAD: 114,
}

# Dreame Vacuum error descriptions
ERROR_CODE_TO_ERROR_DESCRIPTION: Final = {
    DreameVacuumErrorCode.NO_ERROR: ["No error", ""],
    DreameVacuumErrorCode.DROP: [
        "Колёса в воздухе",
        "Поправьте робот-пылесос.",
    ],
    DreameVacuumErrorCode.CLIFF: [
        "Ошибка датчика перепада высоты",
        "Протрите датчик перепада высоты и начните уборку подальше от лестницы.",
    ],
    DreameVacuumErrorCode.BUMPER: [
        "Датчик столкновения застрял",
        "Проверьте, ничего ли не мешает бамперу. Может требуется чистка между корпусом и бампером. Можно попробовать потихоньку постучать по бамперу.",
    ],
    DreameVacuumErrorCode.GESTURE: [
        "Робот-пылесос наклонен",
        "Переместите робот-пылесос на ровную поверхность и запустите снова.",
    ],
    DreameVacuumErrorCode.BUMPER_REPEAT: [
        "Бампер застрял повторно",
        "Проверьте, ничего ли не мешает бамперу. Может требуется чистка между корпусом и бампером. Можно попробовать потихоньку постучать по бамперу.",
    ],
    DreameVacuumErrorCode.DROP_REPEAT: [
        "Колеса в воздухе повторно",
        "Поправьте робот-пылесос.",
    ],
    DreameVacuumErrorCode.OPTICAL_FLOW: [
        "Ошибка оптического датчика",
        "Попробуйте перезагрузить робот-пылесос.",
    ],
    DreameVacuumErrorCode.BOX: [
        "Пылесборник не установлен",
        "Установите пылесборник и фильтр.",
    ],
    DreameVacuumErrorCode.TANKBOX: [
        "Бак для воды не установлен",
        "Установите бак для воды.",
    ],
    DreameVacuumErrorCode.WATERBOX_EMPTY: [
        "Бак для воды пуст",
        "Наполните бак для воды",
    ],
    DreameVacuumErrorCode.BOX_FULL: [
        "Фильтр мокрый или засорился",
        "Проверьте не мокрый ли фильтр и не нуждается ли он в чистке.",
    ],
    DreameVacuumErrorCode.BRUSH: [
        "Проблема с основной щёткой",
        "Снимите основную щетку (которая большая снизу) и очистите ее щетину и подшипники.",
    ],
    DreameVacuumErrorCode.SIDE_BRUSH: [
        "Проблема с боковой щёткой",
        "Снимите и очистите боковую щетку.",
    ],
    DreameVacuumErrorCode.FAN: [
        "Фильтр мокрый или засорился",
        "Проверьте не мокрый ли фильтр и не нуждается ли он в чистке.",
    ],
    DreameVacuumErrorCode.LEFT_WHEEL_MOTOR: [
        "Левое колесо не двигается",
        "Проверьте, не застрял ли какой-либо предмет в левом колесе. И запустите продолжение уборки",
    ],
    DreameVacuumErrorCode.RIGHT_WHEEL_MOTOR: [
        "Правое колесо не двигается",
        "Проверьте, не застрял ли какой-либо предмет в правом колесе. И запустите продолжение уборки",
    ],
    DreameVacuumErrorCode.TURN_SUFFOCATE: [
        "Робот-пылесос застрял и не может развернуться",
        "Проверьте его.",
    ],
    DreameVacuumErrorCode.FORWARD_SUFFOCATE: [
        "Не получается продолжить движение",
        "Проверьте робот-пылесос.",
    ],
    DreameVacuumErrorCode.CHARGER_GET: [
        "Не получается найти зарядную станцию",
        "Проверьте подключено ли электропитание к станции.",
    ],
    DreameVacuumErrorCode.BATTERY_LOW: [
        "Низкий заряд",
        "Требуется зардка.",
    ],
    DreameVacuumErrorCode.CHARGE_FAULT: [
        "Ошибка зарядки",
        "Протрите сухой тканью контакты на робот-пылесосе и на станции.",
    ],
    DreameVacuumErrorCode.BATTERY_PERCENTAGE: ["", ""],
    DreameVacuumErrorCode.HEART: [
        "Внутренняя ошибка",
        "Попробуйте перезагрузить робот-пылесос.",
    ],
    DreameVacuumErrorCode.CAMERA_OCCLUSION: [
        "Ошибка датчика визуального позиционирования",
        "Попробуйте протереть его.",
    ],
    DreameVacuumErrorCode.MOVE: [
        "Ошибка датчика перемещения",
        "Попробуйте перезагрузить робот-пылесос.",
    ],
    DreameVacuumErrorCode.FLOW_SHIELDING: [
        "Ошибка оптического датчика",
        "Попробуйте протереть оптический датчик и перезагрузить робот-пылесос.",
    ],
    DreameVacuumErrorCode.INFRARED_SHIELDING: [
        "Ошибка инфракрасного датчика",
        "Попробуйте перезагрузить робот-пылесос.",
    ],
    DreameVacuumErrorCode.CHARGE_NO_ELECTRIC: [
        "Зарядная док-станция не включена",
        "Проверьте электропитание станции.",
    ],
    DreameVacuumErrorCode.BATTERY_FAULT: [
        "Ошибка температуры батареи",
        "Подождите, пока температура не вернётся в норму.",
    ],
    DreameVacuumErrorCode.FAN_SPEED_ERROR: [
        "Ошибка датчика скорости вентилятора",
        "Попробуйте перезагрузить робот-пылесос.",
    ],
    DreameVacuumErrorCode.LEFTWHELL_SPEED: [
        "Левое колесо, похоже, заблокировано посторонними предметами",
        "Проверьте, не застрял ли какой-либо предмет в левом колесе. И запустите продолжение уборки",
    ],
    DreameVacuumErrorCode.RIGHTWHELL_SPEED: [
        "Правое колесо, похоже, заблокировано посторонними предметами",
        "Проверьте, не застрял ли какой-либо предмет в правом колесе. И запустите продолжение уборки",
    ],
    DreameVacuumErrorCode.BMI055_ACCE: [
        "Ошибка акселерометраr",
        "Попробуйте перезагрузить робот-пылесос. Ещё можно попробовать немного постучать по нему",
    ],
    DreameVacuumErrorCode.BMI055_GYRO: [
        "Ошибка гироскопа",
        "Попробуйте перезагрузить робот-пылесос. Ещё можно попробовать немного постучать по нему",
    ],
    DreameVacuumErrorCode.XV7001: [
        "Ошибка гироскопа",
        "Попробуйте перезагрузить робот-пылесос. Ещё можно попробовать немного постучать по нему",
    ],
    DreameVacuumErrorCode.LEFT_MAGNET: [
        "Ошибка датчика левого магнита",
        "Попробуйте перезагрузить робот-пылесос. Ещё можно попробовать немного постучать по нему",
    ],
    DreameVacuumErrorCode.RIGHT_MAGNET: [
        "Ошибка датчика правого магнита",
        "Попробуйте перезагрузить робот-пылесос. Ещё можно попробовать немного постучать по нему",
    ],
    DreameVacuumErrorCode.FLOW_ERROR: [
        "Ошибка датчика потока",
        "Попробуйте перезагрузить робот-пылесос. Ещё можно попробовать немного постучать по нему",
    ],
    DreameVacuumErrorCode.INFRARED_FAULT: [
        "Ошибка инфракрасного датчика",
        "Попробуйте перезагрузить робот-пылесос. Ещё можно попробовать немного постучать по нему",
    ],
    DreameVacuumErrorCode.CAMERA_FAULT: [
        "Ошибка камеры",
        "Попробуйте перезагрузить робот-пылесос. Ещё можно попробовать немного постучать по нему",
    ],
    DreameVacuumErrorCode.STRONG_MAGNET: [
        "Обнаружено сильное магнитное поле",
        "Попробуйте начать от виртуальной стены.",
    ],
    DreameVacuumErrorCode.WATER_PUMP: [
        "Ошибка водяного насоса",
        "Попробуйте перезагрузить робот-пылесос. Ещё можно попробовать немного постучать по нему",
    ],
    DreameVacuumErrorCode.RTC: ["Ошибка RTC", "Попробуйте перезагрузить робот-пылесос."],
    DreameVacuumErrorCode.AUTO_KEY_TRIG: [
        "Внутренняя ошибка",
        "Попробуйте перезагрузить робот-пылесос. Ещё можно попробовать немного постучать по нему",
    ],
    DreameVacuumErrorCode.P3V3: [
        "Внутренняя ошибка",
        "Попробуйте перезагрузить робот-пылесос. Ещё можно попробовать немного постучать по нему",
    ],
    DreameVacuumErrorCode.CAMERA_IDLE: [
        "Внутренняя ошибка",
        "Попробуйте перезагрузить робот-пылесос. Ещё можно попробовать немного постучать по нему",
    ],
    DreameVacuumErrorCode.BLOCKED: [
        "Route notification",
        "Маршрут уборки заблокирован, возвращение на станцию...",
    ],
    DreameVacuumErrorCode.LDS_ERROR: [
        "Ошибка лазерного датчика расстояния",
        "Проверьте, нет ли в лазерном датчике расстояния застрявших предметов",
    ],
    DreameVacuumErrorCode.LDS_BUMPER: [
        "Ошибка бампера лазерного датчика расстояния",
        "Проверьте, не застрял ли бампер лазерного датчика расстояния",
    ],
    DreameVacuumErrorCode.WATER_PUMP_2: [
        "Ошибка водяного насоса. 2",
        "Попробуйте перезагрузить робот-пылесос. Ещё можно попробовать немного постучать по нему",
    ],
    DreameVacuumErrorCode.FILTER_BLOCKED: [
        "Фильтр мокрый или засорился",
        "Проверьте не мокрый ли фильтр и не нуждается ли он в чистке.",
    ],
    DreameVacuumErrorCode.EDGE: [
        "Ошибка датчика края",
        "Проверьте и протрите его.",
    ],
    DreameVacuumErrorCode.CARPET: [
        "Запустите робот-пылесос в зоне, свободной от ковров.",
        "Во время мытья полов под роботом обнаруживается ковер. Переместите робот-пылесос в другое место и перезапустите его.",
    ],
    DreameVacuumErrorCode.LASER: [
        "Неисправен 3D-датчик обхода препятствий.",
        "Попробуйте протереть 3D-датчик обхода препятствий и перезагрузить робот-пылесос.",
    ],
    DreameVacuumErrorCode.EDGE_2: [
        "Ошибка датчика края. 2",
        "Проверьте и протрите его.",
    ],
    DreameVacuumErrorCode.ULTRASONIC: [
        "Ультразвуковой датчик неисправен.",
        "Попробуйте перезагрузить робот-пылесос. Ещё можно попробовать немного постучать по нему",
    ],
    DreameVacuumErrorCode.NO_GO_ZONE: [
        "Обнаружена запретная зона или виртуальная стена.",
        "Вынесите робот-пылесос из этой зоны и попробуйте ещё раз.",
    ],
    DreameVacuumErrorCode.ROUTE: [
        "Маршрут уборки заблокирован.",
        "Убедитесь, что все двери в доме открыты и устраните все препятствия на пути.",
    ],
    DreameVacuumErrorCode.ROUTE_2: [
        "Маршрут уборки заблокирован.",
        "Убедитесь, что все двери в доме открыты и устраните все препятствия на пути.",
    ],
    DreameVacuumErrorCode.BLOCKED_2: [
        "Маршрут уборки заблокирован. 2.",
        "Убедитесь, что все двери в доме открыты и устраните все препятствия на пути.",
    ],
    DreameVacuumErrorCode.BLOCKED_3: [
        "Маршрут уборки заблокирован. 3.",
        "Убедитесь, что все двери в доме открыты и устраните все препятствия на пути. Попробуйте удалить зону с ограниченным доступом или переместите робот-пылесос из этой зоны",
    ],
    DreameVacuumErrorCode.RESTRICTED: [
        "Обнаружено, что пылесос находится в запретной зоне.",
        "Переместите робот-пылесос из этой зоны.",
    ],
    DreameVacuumErrorCode.RESTRICTED_2: [
        "Обнаружено, что пылесос находится в запретной зоне. 2.",
        "Переместите робот-пылесос из этой зоны.",
    ],
    DreameVacuumErrorCode.RESTRICTED_3: [
        "Обнаружено, что пылесос находится в запретной зоне. 3.",
        "Переместите робот-пылесос из этой зоны.",
    ],
    DreameVacuumErrorCode.REMOVE_MOP: [
        "Уборка завершена. Промывайте тряпки швабры почаще.",
        "",
    ],
    DreameVacuumErrorCode.MOP_REMOVED: [
        "Швабра отсоединилась во время уборки.",
        "Установите их обратно перед возобновлением уборки.",
    ],
    DreameVacuumErrorCode.MOP_REMOVED_2: [
        "Швабра отсоединилась во время уборки. 2.",
        "Установите их обратно перед возобновлением уборки.",
    ],
    DreameVacuumErrorCode.MOP_PAD_STOP_ROTATE: [
        "Швабры перестали вращаться",
        "Устраните проблему.",
    ],
    DreameVacuumErrorCode.MOP_PAD_STOP_ROTATE_2: [
        "Швабры перестали вращаться. 2",
        "Устраните проблему.",
    ],
    DreameVacuumErrorCode.BIN_FULL: [
        "Пылесборник переполнен или засорён воздуховод или фильтр.",
        "Устраните проблему.",
    ],
    DreameVacuumErrorCode.BIN_OPEN: [
        "Верхняя крышка модуля подключения к водопроводу не закрыта или не установлен пылесборник.",
        "Установите пылесборник должным образом и закройте крышку модуля подключения к водопроводу.",
    ],
    DreameVacuumErrorCode.BIN_OPEN_2: [
        "Верхняя крышка модуля подключения к водопроводу не закрыта или не установлен пылесборник. 2",
        "Установите пылесборник должным образом и закройте крышку модуля подключения к водопроводу.",
    ],
    DreameVacuumErrorCode.BIN_FULL_2: [
        "Пылесборник переполнен или засорён воздуховод или фильтр. 2.",
        "Устраните проблему.",
    ],
    DreameVacuumErrorCode.WATER_TANK: [
        "Бак для чистой воды не установлен.",
        "Наполните бак для чистой воды и становите его должным образом.",
    ],
    DreameVacuumErrorCode.DIRTY_WATER_TANK: [
        "Бак для грязной воды не установлен.",
        "Опорожните бак для грязной воды и установите его должным образом.",
    ],
    DreameVacuumErrorCode.WATER_TANK_DRY: [
        "Низкий уровень воды в баке для чистой воды.",
        "Если срочно не долить воды, то робот-пылесос не вернётся на базу для очистки швабры во время уборки, а вернётся только в конце уборки.",
    ],
    DreameVacuumErrorCode.DIRTY_WATER_TANK_BLOCKED: [
        "Бак для грязной воды заблокирован.",
        "Попробуйте перезагрузить станцию и робот-пылесос. Ещё можно попробовать немного постучать по ним",
    ],
    DreameVacuumErrorCode.DIRTY_WATER_TANK_PUMP: [
        "Ошибка насоса бака для грязной воды.",
        "Попробуйте перезагрузить станцию и робот-пылесос. Ещё можно попробовать немного постучать по ним",
    ],
    DreameVacuumErrorCode.MOP_PAD: [
        "Стиральная доска установлена неправильно.",
        "Стиральная доска (которая под швабрами) установлена не правильно или не установлена. Убедитесь, что стиральная доска установлена и что застежки с обеих сторон надежно защёлкнуты.",
    ],
    DreameVacuumErrorCode.WET_MOP_PAD: [
        "Уровень воды в стриральной доске под швабрами ненормальный.",
        "Удалите воду в стиральной доске (которая под швабрами) вручную. Если не помогло, то надо везти в сервисный центр. Почаще очищайте доску для чистки швабр.",
    ],
    DreameVacuumErrorCode.CLEAN_MOP_PAD: [
        "Уборка завершена. Снимите и промойте швабры",
        "Очищайте стиральную доску под швабрами вовремя, чтобы избежать сильного загрязнения и запаха",
    ],
    DreameVacuumErrorCode.CLEAN_TANK_LEVEL: [
        "Чистая вода закончилась.",
        "Заполните бак для чистой воды. Заодно и грязную можно вылить.",
    ],
    DreameVacuumErrorCode.DIRTY_TANK_LEVEL: [
        "Бак с грязной водой полон.",
        "Опустошите бак с грязной водой.",
    ],
    DreameVacuumErrorCode.WASHBOARD_LEVEL: [
        "Уровень воды в стриральной доске слишком большой.",
        "Очистите стиральную доску, которая под швабрами. И почаще мойте её, чтобы не было засоров.",
    ],
}
