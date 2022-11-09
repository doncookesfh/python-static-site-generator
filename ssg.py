import typer
import ssg.site

def main(source, dest):
    config = {'source' : source, 'dest' : dest}
    site = site().build()

typer.run(main())