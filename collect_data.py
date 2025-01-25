import subprocess

task_names = ["sweep", "cabinet", "sort", "rope", "sandwich", "pack"]
temperature = 0.7
num_runs = 3
run_name = "qwq"

llm_source = "qwen2.5:32b"

for task_name in task_names:
    cmd = f"python run_dialog.py --run_name {run_name} --llm_source {llm_source} --temperature {temperature} --task {task_name} -sd --num_runs {num_runs}"
    print(f"running: {cmd}")  # just in case you wanna debug
    subprocess.run(cmd, shell=True, check=True)
