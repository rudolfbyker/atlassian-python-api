import os

from atlassian.bitbucket import Cloud

if __name__ == '__main__':
    bb = Cloud(
        username=os.environ["BB_USERNAME"],
        password=os.environ["BB_PASSWORD"],
        cloud=True,
    )

    all_workspaces = list(bb.workspaces.each())
    names = [workspace.name for workspace in all_workspaces]

    print(all_workspaces)
