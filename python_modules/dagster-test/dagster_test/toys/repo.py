from dagster_examples.toys.hammer import hammer_pipeline
from dagster_test.toys.composition import composition
from dagster_test.toys.error_monster import error_monster
from dagster_test.toys.fan_in_fan_out import fan_in_fan_out_pipeline
from dagster_test.toys.log_spew import log_spew
from dagster_test.toys.many_events import many_events
from dagster_test.toys.sleepy import sleepy_pipeline

from dagster import repository


@repository
def toys_repository():
    return [
        composition,
        error_monster,
        hammer_pipeline,
        fan_in_fan_out_pipeline,
        log_spew,
        many_events,
        sleepy_pipeline,
    ]