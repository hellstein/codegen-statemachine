# How to use ?

* State declaration
```json
[
    {
        state:
        description:
        definition:
    },
    {
        state:
        description:
        definition:
    }   
]
```

* Transition declaration
```json
[
    { 
        state:
        action:
        success: {
            validation:
            state:
        },
        fail: [
            {
                validation:
                state:
            }
        ]
    },
    { 
        state:
        action:
        success: {
            validation:
            state:
        },
        fail: [
            {
                validation:
                state:
            }
        ]
    }
]
```

