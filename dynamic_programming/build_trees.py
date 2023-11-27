import graphviz

dot = graphviz.Digraph(
    'justice league', 
    comment='The Justice League', 
    node_attr={'shape':'plaintext'},
    format='png'
    )

dot.attr('node', shape='rarrow')
dot.node('A', 'Spiderman')
dot.edge('B','L', constraint='false')
dot.node('B', 'Batman')
dot.attr('node', shape='star')
dot.node('L', 'Flash',shape='egg')

dot.edges(['AB','AL'])


dot.graph_attr['rankdir'] = 'LR'
dot.edge_attr.update(arrowhead='vee',arrowsize='2')
print(dot.source)
dot.render(directory='doctest-output').replace('\\','/')