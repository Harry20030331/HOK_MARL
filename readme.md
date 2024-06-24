# project title
HOK_MARL

# project description
this is the HOK GAME project, the final project of multi agent system class at Peking University.

# getting started
make sure you have the image env of demo_name

# training model
revise "args" in .vscode/launch.json
give an example below:
 "args": [
        "--config=vdn",
        "--env-config=hok",
        "with",
        "env_args.map_name=hok",
            ]
(we support four different algothrims:vdn,nmix,qatten,qmix)

# testing model
revise "args" in .vscode/launch.json
give an example below:
 "args": [
        "--evaluate=true",
        "--checkpoint_path=results/models/vdn_env__2024-06-22_03-54-35/338250",
        "--test_nepisode=20",
        "--config=vdn",
        "--env-config=hok",
        "with",
        "env_args.map_name=hok",
            ]
(make sure "checkpoint_path" exsits)

# author
yuming feng, jinghan gan