import graphene

import graphql_countries


class Query(graphene.ObjectType, graphql_countries.Query):
    pass


schema = graphene.Schema(query=Query)
