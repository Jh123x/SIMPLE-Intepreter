import os
from main import run, tokenizer


if __name__ == "__main__":
    test_dir = os.path.join(".", 'tests')
    for filename in os.listdir(test_dir):
        full_path = os.path.join(test_dir, filename)
        
        try: 
            print(f"Running tests on {full_path}")
            run(full_path)
            print(f"Passed")
        except Exception as e:
            print("Failed")
            try:
                for item in tokenizer(full_path):
                    print(item)
            except:
                print("Lexor issue")
            print(f"Error encountered in {full_path}: {e.with_traceback(None)}")    