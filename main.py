from streamlit.web.cli import main
import sys


if __name__ == "__main__":
    sys.argv = ["streamlit", "run", "web.py", ""]
    sys.exit(main(prog_name="streamlit"))
