gunnar = sum(map(int, input().split()))
emma = sum(map(int, input().split()))

if gunnar > emma:
    print("Gunnar")
elif gunnar == emma:
    print("Tie")
else:
    print("Emma")