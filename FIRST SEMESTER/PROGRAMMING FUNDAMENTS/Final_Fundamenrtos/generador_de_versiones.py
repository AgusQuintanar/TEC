from git import RemoteProgress

class MyProgressPrinter(RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        print(op_code, cur_count, max_count, cur_count / (max_count or 100.0), message or "NO MESSAGE")
# end
self.assertEqual(len(cloned_repo.remotes), 1) # we have been cloned, so should be one remote
self.assertEqual(len(bare_repo.remotes), 0) # this one was just initialized
origin = bare_repo.create_remote('origin', url=cloned_repo.working_tree_dir)
assert origin.exists()
for fetch_info in origin.fetch(progress=MyProgressPrinter()):
    print("Updated %s to %s" % (fetch_info.ref, fetch_info.commit))
# create a local branch at the latest fetched master. We specify the name statically, but you have all
# information to do it programatically as well.
bare_master = bare_repo.create_head('master', origin.refs.master)
bare_repo.head.set_reference(bare_master)
assert not bare_repo.delete_remote(origin).exists()
# push and pull behave very similarly
