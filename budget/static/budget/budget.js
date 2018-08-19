document.addEventListener('DOMContentLoaded', ()=> {
    const DOM = {
        category_groups: document.querySelector('.categorie_group'),
        category: document.querySelector('.category')
    }

    function createCategoryGroup(category_name) {
        const elem = document.createElement('div');
        elem.appendChild(document.createTextNode(category_name));
        elem.className = category_name;
        return elem;
    }

    function addCategoryGroupToDOM(category_name) {
        const elem = DOM.category_groups;
        elem.appendChild(createCategoryGroup(category_name));
    }

    // Nests some category inside a category group
    function createCategory(category) {
        const elem = document.createElement('div');
        elem.appendChild(document.createTextNode(category));
        elem.className = 'category';
        return elem;
    }

    // Creates a budgeting category
    function addCategoryToDOM(category_group, category) {
        const elem = document.getElementsByClassName(category_group);
        elem[0].appendChild(createCategory(category));
    }

    document.getElementById('submit_category_group').onclick = () => {
        const category_group = document.getElementById('category_group').value;
        addCategoryGroupToDOM(category_group);
    }

    document.getElementById('submit_category').onclick = () => {
        const category = document.getElementById('category').value;
        const parent_group = document.getElementById('super').value;
        addCategoryToDOM(parent_group, category)
    }
});