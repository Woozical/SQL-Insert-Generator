from random import random, choice, randint

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def generateText(limit=100):
    output = ""
    for i in range (randint(1,limit)):
        output = output + choice(ALPHABET)

    return output


def write_seed_file(db:str, table:str, columns:list, file_name:str='gen_seed', entries:int=100):
    """
    Writes a basic SQL script in the same directory to populate a table with junk data.

    Parameters:
        db (string): Name of the database the script will connect to.
        
        table (string): Name of the table to insert into.
        
        columns (list): A list of tuples.
        First element is column name, as a string.
        Second element is column type, pass in the Python type class. (Supported: str, int, bool, float).
        Third element is character limit of text, or max value of a number. Should be supplied as an integer, can be left empty.
        
        file_name(string): The name of the output file, file extension added automatically. (DEFAULT: gen_seed.sql)
        
        entries(int): The number of entries to insert into the table (DEFAULT: 100)
    
    Example call:
        write_seed_file(db = "testing_db", table = "my_kittens", columns = [
            ("name", str),
            ("age", int, 20),
            ("female", bool)])
    
    """
    with open(f'{file_name}.sql', 'w') as file:
        ins_str = f'\c {db};\nINSERT INTO {table} ('
        for column in columns:
            ins_str = ins_str + column[0] + ', '

        ins_str = ins_str.strip(', ') + ') VALUES \n'

        file.write(ins_str)

        for i in range(entries):
            line = '('
            for column in columns:
                col_type = column[1]
                
                try:
                    max = column[2]
                except IndexError:
                    max = 100

                if col_type == str:
                    line = line + f"'{generateText(max)}', "
                elif col_type == bool:
                    line = line + f"{choice(['true', 'false'])}, "
                elif col_type == int:
                    line = line + f"{randint(1, max)}, "
                elif col_type == float:
                    line = line + f"{random() * max}, "
                else:
                    raise Exception(f'Missing or unrecognized column type: {column[1]} on column {column[0]}\n Try str, bool, int, or float.')
            
            if i == entries-1:
                line = line.strip(', ') + ");"
            else:
                line = line.strip(', ') + '),\n'
            file.write(line)