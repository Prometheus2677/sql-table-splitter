def split_sql_file(sql_file):
    delimiter = 'DROP TABLE IF EXISTS'
    with open(sql_file, 'r', encoding='latin-1') as file:
        sql_content = file.read()

    sql_statements = sql_content.split(delimiter)

    for index, statement in enumerate(sql_statements):
        if index == 0:
            continue
        output_file = f'db/output_{index}.sql'
        try:
            with open(output_file, 'w') as file:
                file.write(delimiter + statement)
        except:
            try:
                with open(output_file, 'w', encoding='utf-8') as file:
                    file.write(delimiter + statement)
            except:
                with open(output_file, 'w', encoding='latin-1') as file:
                    file.write(delimiter + statement)


        print(f'Split statement {index} saved to {output_file}')

# Call the function with the SQL file path
sql_file = 'db.sql'
split_sql_file(sql_file)