# Dyalog APL bindings for sqlite3

This repository contains a Dyalog namespace providing bindings to the [sqlite3](https://www.sqlite.org/) embedded database. 

To use it, you need to have sqlite3 installed, and know the location of the sqlite3 DLL. On my mac, I've installed sqlite3 via [homebrew](https://brew.sh), and it lives in 

```apl
lib ← '/opt/homebrew/Cellar/sqlite/3.44.2/lib/libsqlite3.dylib'
```

1. Check out this repositiory
    ```
    git clone git@github.com:xpqz/dyalog-sqlite3.git
    ```
1. In the Dyalog session, [link](https://dyalog.github.io/link) the directory of the repository to your workspace,
    ```
    ]create # work/dyalog-sqlite3 ⍝ Modify to match your path
    ```
1. Initialise the sqlite3 bindings
    ```
    sqlite3.init lib
    ```

You should now be able to use it, for example

```apl
      db ← sqlite3.open 'foo.db'
      sh ← sqlite3.prepare_v2(db 'SELECT SQLITE_VERSION()')
      rc ← sqlite3.step sh
      sqlite3.column_text sh 0
3.44.2
      sqlite3.finalize sh
      sqlite3.close db
```

The function `sqlite3.table` is the one QoL concession beyond the basic API:

```apl
      db ← sqlite3.open 'foo.db'
      sh ← sqlite3.prepare_v2(db 'SELECT * FROM Cars')
      sqlite3.table sh

1  Audi         52642
2  Mercedes     57127
3  Skoda         9000
4  Volvo        29000
5  Bentley     350000
6  Hummer       41400
7  Citroen      21000
8  Volkswagen   21600
9  Tesla        55000
```

It consumes a live statement handle, and returns the contents as an APL array.

## NOTE: THIS IS C!

This tracks the underlying API closely. The values returned by, for example, `prepare_v2` are essentially C pointers. No attempts have been made to protect the APL user from the sharp edges this entails: you need to free up resources you're done with (with `finalize` and `close`). If you free a resource that's already been freed, Bad Things may happen.