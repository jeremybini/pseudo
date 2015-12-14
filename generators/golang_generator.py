from pseudon.code_generator import CodeGenerator


class GolangGenerator(CodeGenerator):

    templates = {
        'program': '%code~join<\n>~'
        'function': 'def %name(%args~join<,>):\n' +
                    '%body~indent<1>~\n'
    }
