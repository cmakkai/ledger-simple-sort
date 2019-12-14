# ledger-simple-sort

## Purpose

This small Python script parses a Ledger (ledger-cli.org) journal and sorts transactions by date without re-formatting the original transactions.

Ledger offers sorting through `ledger print --raw` command, yet doing so strips some data such as comments outside of transactions. This Python script solves this problem by using regular expressions to parse and sort blocks of text.

## Features

Currently this script supports sorting of journal files composed entirely of these 2 types of blocks:

* Transactions
* Comments outside of transactions

## Limitations

There are some valid Ledger entries, such as price db, timelog and automated transactions, that the script does not yet support.

## Author

[Callum Makkai](https://makkai.com) | GitHub: [cmakkai](https://github.com/cmakkai)

## Contributing

I am an amateur programmer and recognize this is a rudimentary effort. I welcome constructive feedback and contributions from the community.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
