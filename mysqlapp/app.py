from Models.customers import database
data = {
    "params":[
        {
            "values" :{
                "username" : "userpertama",
                "namadepan" : "rudi",
                "namabelakang" : "roundhouse",
                "email" : "rudi.roundhouse@gmail.com"
            } 
        },
        {
            "values" :{
                "username" : "userkeempat",
                "namadepan" : "samid",
                "namabelakang" : "samiddd",
                "email" : "shiroe.ishigami@gmail.com"
            } 
        },
        
    ]
}
data1 = {
    "params":[
        {
            "userid": 2
        },
        {
            "userid": 8
        }       
    ]
}

def tambahData(data):
    for param in data['params']:
        mysqldb.insertUser(**param)
    mysqldb.dataCommit()
    print("data berhasil ditambahkan")

def ubahData(data):    
    for param in data['params']:
        mysqldb.updateUserById(**param)
    mysqldb.dataCommit()
    print("data berhasil diubah")

def hapusData(data):
    for param in data['params']:
        mysqldb.deleteUserById(**param)
    mysqldb.dataCommit()
    print("data berhasil dihapus")

def tampilData(data):
    for param in data['params']:
        mysqldb.showUserById(**param)
    mysqldb.dataCommit()
    print("data berhasil tampilkan")



if __name__ == "__main__":
    mysqldb = database()
    if mysqldb.db.is_connected():
        print('Connected to MySQL database')
    
    # tambahData(data)
    # tampilData(data1)
    tampung = database()
    tampung.showUsers()
    #isi dengan fungsi yang kalian butuhkan
    #jangan lupa untuk menyesuaikan isi variabel data dengan struktur data yang dibutuhkan
        
    if mysqldb.db is not None and mysqldb.db.is_connected():
        mysqldb.db.close()