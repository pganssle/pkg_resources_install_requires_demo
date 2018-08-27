try:
    from pkg2 import demo_func
except ImportError:
    def demo_func():
        print("Fell back to pkg1")

def main():
    demo_func()
