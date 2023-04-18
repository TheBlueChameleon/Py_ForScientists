# To fully "appreciate" this example, start it directly from the console by typing
#   python3 Forkbomb_A.py
# You will see two things:
#  - The code crashes with a lengthy error message
#  - The prompt MAIN is written N+1 times (where N is mp.cpu_count). That is because each Process launches THE ENTIRE
#    program, theoretically causing a fork bomb (each process spawns subprocesses which spawn subprocesses which ...)
# In reality, this does not cause a chain reaction because:
#    The parent process waits until all child processes have been started and then tries to terminate.
#    The OS recognizes that the parent process terminates while its child processes are still alive
#    As a consequence, the entire construct is killed, i.e. we get the error message.

import multiprocessing as mp

print(f"MAIN {mp.current_process()}")

def idle():
    print(f"idle {mp.current_process()}")


# There are actually multiple ways of starting a new process. "spawn" is the default one on Windows, which starts the
# entire program new, consistent with what we discussed above. Linux can also do "fork", which is essentially "copy the
# current state into a new process". The current state includes "what's the next instruction to execute", so this would
# bypass the forkbomb problem.
# The below line forces the Windows behaviour.
# Note that the fork method will still cause similar problems when it comes to code on module level, so it's best to
# encapsulate code in functions and classes.
mp.set_start_method('spawn')
processes = [mp.Process(target=idle) for _ in range(mp.cpu_count())]

for p in processes:
    p.start()

for p in processes:
    p.join()
