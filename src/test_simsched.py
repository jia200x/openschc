# C.A. 2018

from simsched import SimulScheduler

scheduler = SimulScheduler()
cancel_event_id = None

def callback(arg1, arg2, scheduler=scheduler):
    global cancel_event_id
    if cancel_event_id != None:
        canceled_event = scheduler.cancel_event(cancel_event_id)
    else:
        canceled_event = None
    print("clock=%s callback, argw=%s next_event_time=%s canceled=%s"%(
        scheduler.get_clock(), repr((arg1, arg2)),
        scheduler.get_next_event_time(), canceled_event))
    if arg1 == "1":
        scheduler.add_event(1, callback, ("2", "two"))
        cancel_event_id = scheduler.add_event(1, callback, ("none", "none"))

scheduler.add_event(3, callback, ("4", "four"))
scheduler.add_event(1, callback, ("1", "one"))
scheduler.run()
