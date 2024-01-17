# Dyalog APL bindings for sqlite3

This repository contains a Dyalog namespace providing bindings to the [sqlite3](https://www.sqlite.org/) embedded database. 

To use it, you need to have sqlite3 installed, and know the location of the sqlite3 DLL. On my mac, I've installed sqlite3 via [homebrew](https://brew.sh), and it lives in 

```
/opt/homebrew/Cellar/sqlite/3.44.2/lib/libsqlite3.dylib
```

1. Check out this repositiory
    ```
    git clone git@github.com:xpqz/dyalog-sqlite3.git
    ```
2. Start Dyalog
3. In the Dyalog session, [link](https://dyalog.github.io/link) the directory of the repository to your workspace,
    ```
    ]create # work/dyalog-sqlite3 ⍝ Modify to match your path
    ```
4. Initialise the sqlite3 bindings
    ```
    sqlite3.init '/opt/homebrew/Cellar/sqlite/3.44.2/lib/libsqlite3.dylib' ⍝ Modify to match your path
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