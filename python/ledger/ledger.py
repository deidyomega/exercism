# -*- coding: utf-8 -*-
from datetime import datetime


class LedgerEntry(object):
    def __init__(self):
        self.date = None
        self.description = None
        self.change = None


def create_entry(date, description, change):
    entry = LedgerEntry()
    entry.date = datetime.strptime(date, '%Y-%m-%d')
    entry.description = description
    entry.change = change
    return entry

def format_entry(entry_descipt):
    if len(entry_descipt) > 25:
        return entry_descipt[0:22] + "..."
    else:
        return entry_descipt.ljust(25, " ")

def get_next_entry(entries):
    for i in range(len(entries)):
        entry = entries[i]
        min_entry = entries[0]
        if entry.date < min_entry.date:
            return i
        if entry.date == min_entry.date:
            if entry.change < min_entry.change:
                return i
            if entry.description < min_entry.description:
                return i
    return 0

def format_entries(currency, locale, entries):
    if locale == 'en_US':
        # Generate Header Row
        table = 'Date       | Description               | Change       '

        while len(entries) > 0:
            table += '\n'

            # Find next entry in order
            min_entry_index = get_next_entry(entries)
            entry = entries[min_entry_index]
            entries.pop(min_entry_index)

            # Write entry date to table            
            table += f"{entry.date.month:02}/{entry.date.day:02}/{entry.date.year:4} | "
            table += format_entry(entry.description) + ' | '

            # Write entry change to table
            if currency == 'USD':
                change_str = ''
                if entry.change < 0:
                    change_str = '('
                change_str += '$'
                change_dollar = abs(int(entry.change / 100.0))
                dollar_parts = []
                while change_dollar > 0:
                    dollar_parts.insert(0, str(change_dollar % 1000))
                    change_dollar = change_dollar // 1000
                if len(dollar_parts) == 0:
                    change_str += '0'
                else:
                    while True:
                        change_str += dollar_parts[0]
                        dollar_parts.pop(0)
                        if len(dollar_parts) == 0:
                            break
                        change_str += ','
                change_str += '.'
                change_cents = abs(entry.change) % 100
                change_cents = str(change_cents)
                if len(change_cents) < 2:
                    change_cents = '0' + change_cents
                change_str += change_cents
                if entry.change < 0:
                    change_str += ')'
                else:
                    change_str += ' '
                while len(change_str) < 13:
                    change_str = ' ' + change_str
                table += change_str
            elif currency == 'EUR':
                change_str = ''
                if entry.change < 0:
                    change_str = '('
                change_str += u'€'
                change_euro = abs(int(entry.change / 100.0))
                euro_parts = []
                while change_euro > 0:
                    euro_parts.insert(0, str(change_euro % 1000))
                    change_euro = change_euro // 1000
                if len(euro_parts) == 0:
                    change_str += '0'
                else:
                    while True:
                        change_str += euro_parts[0]
                        euro_parts.pop(0)
                        if len(euro_parts) == 0:
                            break
                        change_str += ','
                change_str += '.'
                change_cents = abs(entry.change) % 100
                change_cents = str(change_cents)
                if len(change_cents) < 2:
                    change_cents = '0' + change_cents
                change_str += change_cents
                if entry.change < 0:
                    change_str += ')'
                else:
                    change_str += ' '
                while len(change_str) < 13:
                    change_str = ' ' + change_str
                table += change_str
        return table
    elif locale == 'nl_NL':
        # Generate Header Row
        table = 'Datum      | Omschrijving              | Verandering  '

        while len(entries) > 0:
            table += '\n'

            # Find next entry in order
            min_entry_index = get_next_entry(entries)
            entry = entries[min_entry_index]
            entries.pop(min_entry_index)

            # Write entry date to table
            table += f"{entry.date.day:02}-{entry.date.month:02}-{entry.date.year:4} | "
            table += format_entry(entry.description) + ' | '

            # Write entry change to table
            if currency == 'USD':
                change_str = '$ '
                if entry.change < 0:
                    change_str += '-'
                change_dollar = abs(int(entry.change / 100.0))
                dollar_parts = []
                while change_dollar > 0:
                    dollar_parts.insert(0, str(change_dollar % 1000))
                    change_dollar = change_dollar // 1000
                if len(dollar_parts) == 0:
                    change_str += '0'
                else:
                    while True:
                        change_str += dollar_parts[0]
                        dollar_parts.pop(0)
                        if len(dollar_parts) == 0:
                            break
                        change_str += '.'
                change_str += ','
                change_cents = abs(entry.change) % 100
                change_cents = str(change_cents)
                if len(change_cents) < 2:
                    change_cents = '0' + change_cents
                change_str += change_cents
                change_str += ' '
                while len(change_str) < 13:
                    change_str = ' ' + change_str
                table += change_str
            elif currency == 'EUR':
                change_str = u'€ '
                if entry.change < 0:
                    change_str += '-'
                change_euro = abs(int(entry.change / 100.0))
                euro_parts = []
                while change_euro > 0:
                    euro_parts.insert(0, str(change_euro % 1000))
                    change_euro = change_euro // 1000
                if len(euro_parts) == 0:
                    change_str += '0'
                else:
                    while True:
                        change_str += euro_parts[0]
                        euro_parts.pop(0)
                        if len(euro_parts) == 0:
                            break
                        change_str += '.'
                change_str += ','
                change_cents = abs(entry.change) % 100
                change_cents = str(change_cents)
                if len(change_cents) < 2:
                    change_cents = '0' + change_cents
                change_str += change_cents
                change_str += ' '
                while len(change_str) < 13:
                    change_str = ' ' + change_str
                table += change_str
        
        return table
