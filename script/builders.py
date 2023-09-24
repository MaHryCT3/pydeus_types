from genson import SchemaBuilder

from script.strategies import LinksStrategy, LinkInValuesStrategy


class ModeusSchemaBuilder(SchemaBuilder):
    STRATEGIES = (LinksStrategy, LinkInValuesStrategy) + SchemaBuilder.STRATEGIES
