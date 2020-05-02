import axios from "axios";
//csrftoken

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
let csrftoken = getCookie("csrftoken");
//End csrftoken

function getCities() {
  const cityList = document.querySelector(".city__list");

  fetch("/locations/city/api/")
    .then(function(response) {
      return response.json();
    })
    .then(function(data) {
      data.cities.forEach(city => {
        const cityItem = document.createElement("li");

        cityItem.classList.add("city__item");
        cityItem.textContent = city.name;
        cityItem.setAttribute("data-slug", city.slug);
        cityItem.setAttribute("data-id", city.id);
        cityList.append(cityItem);
      });

      saveCity(cityList);
    })
    .catch(function(err) {
      console.warn("Something went wrong.", err);
    });
}

function saveCity(city) {
  if (city) {
    city.childNodes.forEach(element => {
      element.addEventListener("click", event => {
        const target = event.target;
        if (event.target.tagName.toLowerCase() === "li") {
          let cityId = target.getAttribute("data-id");
          let citySlug = target.getAttribute("data-slug");
          let cityName = target.textContent;

          document.querySelector(".location__btn").textContent = cityName;

          axios
            .get(citySaveUrl, {
              params: {
                city_id: cityId,
                city_slug: citySlug,
                city_name: cityName
              }
            })
            .then(function(response) {
              document.location.assign(`/${response.data.city_slug}/`);
            })
            .catch(function(error) {
              console.log(error);
            })
            .then(function() {
              // always executed
            });
        }
      });
    });
  }
}

function getSearch() {
  const inputSearch = document.querySelector(".search__input");
  const dropdownSearchResult = document.querySelector(
    ".search__dropdown-result"
  );

  const dropdownSearchClinics = document.querySelector(
    ".search__dropdown-clinics"
  );
  const dropdownSearchServices = document.querySelector(
    ".search__dropdown-services"
  );
  const dropdownSearchDoctors = document.querySelector(
    ".search__dropdown-doctors"
  );
  const btnSearch = document.querySelector(".search__btn");

  const showSearchClinics = (input, list, data) => {
    list.textContent = "";

    if (input.value !== "") {
      const searchResult = data.filter(item => {
        const ItemName = item.name.toLowerCase();
        return ItemName.includes(input.value.toLowerCase());
      });

      searchResult.forEach(item => {
        const link = document.createElement("a");
        link.classList.add("search__dropdown-item");
        link.textContent = item.name;
        link.href = `/${currentCitySlug}/${item.slug}`;
        list.append(link);
      });
    }
  };

  const showSearchServices = (input, list, data) => {
    list.textContent = "";

    if (input.value !== "") {
      const searchResult = data.filter(item => {
        const ItemName = item.name.toLowerCase();
        return ItemName.includes(input.value.toLowerCase());
      });

      searchResult.forEach(item => {
        const link = document.createElement("a");
        link.classList.add("search__dropdown-item");
        link.textContent = item.name;
        link.href = `/${currentCitySlug}/${item.slug}`;
        list.append(link);
      });
    }
  };

  const showSearchDoctors = (input, list, data) => {
    list.textContent = "";

    if (input.value !== "") {
      const searchResult = data.filter(item => {
        const ItemName = item.user.full_name.toLowerCase();
        return ItemName.includes(input.value.toLowerCase());
      });

      searchResult.forEach(item => {
        const link = document.createElement("a");
        link.classList.add("search__dropdown-item");
        link.textContent = item.user.full_name;
        link.href = `/${currentCitySlug}/vrach/${item.user.slug}`;
        list.append(link);
      });
    }
  };

  fetch("/api/")
    .then(function(response) {
      return response.json();
    })
    .then(function(data) {
      inputSearch.addEventListener("input", () => {
        if (inputSearch.value.length > 0) {
          dropdownSearchResult.style.display = "block";

          showSearchClinics(inputSearch, dropdownSearchClinics, data.clinics);
          showSearchServices(inputSearch, dropdownSearchServices, data.services);
          showSearchDoctors(inputSearch, dropdownSearchDoctors, data.doctors);
        } else {
          dropdownSearchResult.style.display = "none";
        }
      });

      // dropdownSearchResult.addEventListener("click", event => {
      //   const target = event.target;
      //   if (target.tagName.toLowerCase() === "li") {
      //     inputSearch.value = target.textContent;
      //     btnSearch.click();
      //   }
      // });
    })
    .catch(function(err) {
      console.warn("Something went wrong.", err);
    });
}

getCities();
saveCity();
getSearch();

// Модальное окно "Выберите свой город"
function modalCity() {
  const modal = document.querySelector(".modal__city");
  const locationBtn = document.querySelector(".location__btn");
  const modalClose = modal.querySelector(".modal__close");

  locationBtn.addEventListener("click", e => {
    e.preventDefault;
    modal.style.display = "flex";
  });

  modalClose.addEventListener("click", e => {
    e.preventDefault;
    modal.style.display = "none";
  });
}
modalCity();
// End Модальное окно "Выберите свой город"

// Модальное окно "Выберите свой город"
function modalDoctor() {
  const modal = document.querySelector(".modal__doctor");
  const modalClose = modal.querySelector(".modal__close");
  const doctorsList = document.querySelectorAll(
    ".doctors__list .doctors__item"
  );
  doctorsList.forEach(item => {
    const doctorBtn = item.querySelector(".doctors__button");
    doctorBtn.addEventListener("click", e => {
      e.preventDefault;
      modal.style.display = "flex";
    });
  });

  modalClose.addEventListener("click", e => {
    e.preventDefault;
    modal.style.display = "none";
  });
}
modalDoctor();
// End Модальное окно "Выберите свой город"


