import pexpect
child = pexpect.spawn("echo myworld")
print(child.expect(["Hello", "Welcome", "Myworld"]))
