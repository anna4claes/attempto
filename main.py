from settings import REPORT_FILE

from core.storage import Storage
from core.tracker import Tracker
from core.statistics import Statistics

from ui.display import Display
from ui.exporter import Exporter

habits = Storage().load()

tracker = Tracker()

stats = Statistics().build(

    habits,

    tracker

)

Display().show(

    habits,

    stats

)

Exporter().save(

    habits,

    stats,

    REPORT_FILE

)
