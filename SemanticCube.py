class SemanticCube:

    def _init_(self):
        self.semanticCube = {
            '+': {
                'int': {
                    'int': 'int',
                    'float': 'float',
                    'string': 'error',
                    'boolean': 'error' 
                }, 
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'error',
                    'boolean': 'error' 
                }, 
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'string',
                    'boolean': 'error' 
                }, 
                'boolean': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error' 
                } 
            },
            '-': {
                'int': {
                    'int': 'int',
                    'float': 'float',
                    'string': 'error',
                    'boolean': 'error' 
                }, 
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'error',
                    'boolean': 'error' 
                }, 
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error' 
                }, 
                'boolean': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error' 
                }
            },
            '*': {
                'int': {
                    'int': 'int',
                    'float': 'float',
                    'string': 'error',
                    'boolean': 'error' 
                }, 
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'error',
                    'boolean': 'error' 
                }, 
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error' 
                }, 
                'boolean': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error' 
                } 
            },
            '/': {
                'int': {
                    'int': 'int',
                    'float': 'float',
                    'string': 'error',
                    'boolean': 'error' 
                }, 
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'error',
                    'boolean': 'error' 
                }, 
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error' 
                }, 
                'boolean': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error' 
                }, 
            },
            '>': {
                'int': {
                    'int': 'boolean',
                    'float': 'boolean',
                    'string': 'error',
                    'boolean': 'boolean' 
                }, 
                'float': {
                    'int': 'boolean',
                    'float': 'boolean',
                    'string': 'error',
                    'boolean': 'boolean' 
                }, 
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error' 
                }, 
                'boolean': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'boolean' 
                }
            },
            '>=': {
                'int': {
                    'int': 'boolean',
                    'float': 'boolean',
                    'string': 'error',
                    'boolean': 'boolean' 
                }, 
                'float': {
                    'int': 'boolean',
                    'float': 'boolean',
                    'string': 'error',
                    'boolean': 'boolean' 
                }, 
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error' 
                }, 
                'boolean': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'boolean' 
                }
            },
            '<': {
                'int': {
                    'int': 'boolean',
                    'float': 'boolean',
                    'string': 'error',
                    'boolean': 'boolean' 
                }, 
                'float': {
                    'int': 'boolean',
                    'float': 'boolean',
                    'string': 'error',
                    'boolean': 'boolean' 
                }, 
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error' 
                }, 
                'boolean': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'boolean' 
                }
            },
            '<='': {
                'int': {
                    'int': 'boolean',
                    'float': 'boolean',
                    'string': 'error',
                    'boolean': 'boolean' 
                }, 
                'float': {
                    'int': 'boolean',
                    'float': 'boolean',
                    'string': 'error',
                    'boolean': 'boolean' 
                }, 
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error' 
                }, 
                'boolean': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'boolean' 
                }
            },
            '==': {
                'int': {
                    'int': 'boolean',
                    'float': 'boolean',
                    'string': 'error',
                    'boolean': 'boolean' 
                }, 
                'float': {
                    'int': 'boolean',
                    'float': 'boolean',
                    'string': 'error',
                    'boolean': 'boolean' 
                }, 
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error' 
                }, 
                'boolean': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'boolean' 
                }
            },
            '!=': {
                'int': {
                    'int': 'boolean',
                    'float': 'boolean',
                    'string': 'error',
                    'boolean': 'boolean' 
                }, 
                'float': {
                    'int': 'boolean',
                    'float': 'boolean',
                    'string': 'error',
                    'boolean': 'boolean' 
                }, 
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error' 
                }, 
                'boolean': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'boolean' 
                }
            },
            'and': {
                'int': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error' 
                }, 
                'float': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error' 
                }, 
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error' 
                }, 
                'boolean': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'boolean' 
                }
            },
            'or': {
                'int': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error' 
                }, 
                'float': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error' 
                }, 
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error' 
                }, 
                'boolean': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'boolean' 
                }
            }
        }
    
    def getValue(self, operator, op1, op2):
        return self.semanticCube[operator][op1][op2]

    def getCube(self):
        return self