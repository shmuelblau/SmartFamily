# smart-family
Web application - for smart family management





# files-structure

families:
    >> table_name
    >> col_table_names
    >> list of family object >>
        >> id
        >> family_name
        >> password


users:
    >> table_name
    >> col_table_names
    >> list of user object >>
        >> id
        >> family_id
        >> first_name
        >> last_name
        >> age
        >> password
        >> status -> flout

tasks:
    >> table_name
    >> col_table_names
    >> list of user object >>
        >> id
        >> user_id
        >> task_name
        >> description
        >> category -> int
        >> status -> bool


functions:
    >> add_(object_name)
    >> update_(object_name)
    >> get_(table_name)_by_id
    >> get_all_(table_name)
    >> get_(table_name)_by_(object_name)_id
    >> delete_(object_name)
 


<!-- ├── static/
│   ├── database/
│   │   ├── python_classes/
│   │   │   ├── family.py
│   │   │   ├── user.py
│   │   │   └── task.py
│   │   ├── smart_family.db
│   │   └── sql_management.py
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   ├ script.js
│   └── images/
│       └── your_image.png
├── templates/
│    └── home.html
├── app.py
└── sql_manager.py -->


