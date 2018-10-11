import printing_functions as p

p.unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
p.completed_models = []

p.print_models(p.unprinted_designs, p.completed_models)
p.show_completed_models(p.completed_models)