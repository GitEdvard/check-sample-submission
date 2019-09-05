import re
from check_sample_submission.excel_formatter import ERROR


class SheetValidator:
    def __init__(self, excel_formatter=None, logger=None):
        self.logger = logger or DefaultLogger()
        self.excel_formatter = excel_formatter or DefaultExcelFormatter()

    def list_faulty(self, contents):
        error_messages = list()
        self.logger.print('Checking forbidden characters in sample names...')
        self.logger.print('Checking volume formatting...')
        self.logger.print('Checking volume within accepted limits...')
        for idx, row in enumerate(contents):
            response = self._check(row, idx)
            if response is not None:
                error_messages.extend(response)

        return error_messages

    def _add(self, msg, error_list):
        if msg is not None:
            error_list.append(msg)

    def _check(self, row, row_idx):
        sample = row[0]
        volume = row[1]
        if sample == '</SAMPLE ENTRIES>':
            return None
        error_messages = list()
        response = self._check_sample_name(sample, row_idx)
        self._add(response, error_messages)

        response = self._check_volume(sample, volume, row_idx)
        self._add(response, error_messages)

        return None if len(error_messages) == 0 else error_messages

    def _check_volume(self, sample, volume, row_idx):
        msg = None
        if not self._is_number(volume):
            msg = '{}\tVolume is not numeric'.format(sample)
            self.excel_formatter.mark_volume(row_idx, ERROR)
        elif str(volume) == 'None':
            msg = '{}\tDo not have volume'.format(sample)
            self.excel_formatter.mark_volume(row_idx, ERROR)

        return msg

    def _is_number(self, value):
        try:
            if str(value) == 'None':
                return True
            elif '.' in value:
                dummy = float(value)
            else:
                dummy = int(value)
            return True
        except ValueError:
            return False

    def _check_sample_name(self, sample, row_idx):
        has_match = re.match('^[a-zA-Z0-9-]+$', sample)
        msg = None
        if has_match is None:
            faulty_tokens = self._faulty_tokens(sample)
            msg = '{}\tHas faulty tokens, \'{}\''.format(sample, faulty_tokens)
            self.excel_formatter.mark_sample(row_idx, ERROR)

        return msg

    def _faulty_tokens(self, faulty_sample):
        faulty_tokens = ''
        for char in faulty_sample:
            regexp = re.match('[a-zA-Z0-9-]', char)
            if regexp is None:
                faulty_tokens += '(space)' if char == ' ' else char
        return faulty_tokens


class DefaultLogger:
    def print(self, msg):
        pass


class DefaultExcelFormatter:
    def __init__(self):
        pass

    def mark_volume(self, row_idx, level):
        pass

    def mark_sample(self, row_idx, level):
        pass
