import justpy as jp
import api, documentation


jp.Route("/", documentation.Doc.serve)
jp.Route("/api", api.Api.serve)
jp.justpy()
