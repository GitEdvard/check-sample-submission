import click
from check_sample_submission.import_excel import ImportSampleSubmission
from check_sample_submission.print_cache import PrintCache


@click.group()
@click.option('--whatif/--not-whatif', default=False)
@click.pass_context
def cli(ctx, whatif):
    ctx.obj['whatif'] = whatif


@cli.command('validate-rml')
@click.argument('file_path')
@click.pass_context
def validate_rml(ctx, file_path):
    sample_column_index = 3
    volume_column_index = 7
    sample_column_name = 'LIBRARY ID'
    validate(sample_column_index, volume_column_index,
             sample_column_name, file_path)


@cli.command('validate-prep')
@click.argument('file_path')
@click.pass_context
def validate_prep(ctx, file_path):
    sample_column_index = 4
    volume_column_index = 6
    sample_column_name = 'SAMPLE ID'
    validate(sample_column_index, volume_column_index,
             sample_column_name, file_path)

@cli.command('version')
@click.pass_context
def validate_prep(ctx):
    # TODO: Fix proper version handling
    print('1.0.0')


def validate(sample_column_index, volume_column_index, sample_column_name,
             file_path):
    logger = DefaultLogger()
    import_excel = ImportSampleSubmission(
        file_path, sample_column_index, volume_column_index,
        sample_column_name, logger=logger)
    error_messages = import_excel.check_faulty_contents()
    if len(error_messages) > 0:
        cache = PrintCache()
        cache.print('These rows were faulty:')
        for smp in error_messages:
            cache.print(smp)
        cache.copy_to_clipboard()
    else:
        print('No errors detected!')
    if not import_excel.save_workbook():
        print('Excel formatting cannot be updated because the file is already open. '
              'Please close the file if you want excel formatting enabled!')


def cli_main():
    cli(obj={})


if __name__ == '__main__':
    cli_main()


class DefaultLogger:
    def print(self, msg):
        pass
