import graphene
import agroApp.schema


class Query(agroApp.schema.Query, graphene.ObjectType):
    pass

class Mutation(agroApp.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
