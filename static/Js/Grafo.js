let a = "{{Nodos|safe}}";
let b = "{{Conexion|safe}}";

console.log(b);

a = a.split(',');
b = b.split(',');


function Grafo() {

    var cy = window.cy = cytoscape({

        container: document.getElementById('cy'),

        layout: {
            name: 'avsdf',
            nodeSeparation: 120
        },

        style: [
            {
                selector: 'node[name]',
                style: {
                    'content': 'data(name)',
                    'text-valign': 'left',
                    'color': '#000000',
                    'background-color': '#3a7ecf'
                }
            },

            {
                selector: 'edge',
                style: {
                    'width': 3,
                    'line-color': 'black',
                    'opacity': 1,
                    'curve-style': 'bezier',
                    'target-arrow-shape': 'triangle',
                }
            }
        ],
    });

    for (let c = 0; c < a.length; c++) {
        var eles = cy.add([
            { group: 'nodes', data: { id: 'v' + a[c], weight: c, name: 'R' + a[c] } }
        ]);
    }


    for (let c = 0; c < b.length; c++) {
        if (c + 1 < b.length) {
            var eles = cy.add([
                { group: 'edges', data: { source: 'v' + b[c], target: 'v' + b[c + 1], directed: 'false' } }
            ]);
            c++;
        }

    }


    var layout = cy.layout({
        name: 'avsdf',
        refresh: 1,
        animate: "end",
        animationDuration: 1000,
        animationEasing: 'ease-in-out',
        nodeSeparation: 120
    });

    layout.run();

}