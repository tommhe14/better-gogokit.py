from bs4 import BeautifulSoup

class Helper:
    """
    A helper class that provides utility functions like converting objects to dictionaries.
    """
    def object_to_dict(self, obj):
        """
        Convert a given object (or its attributes) to a dictionary, including nested objects.
        Handles 'gogokit.hal.Link' objects explicitly.
        """
        from gogokit.hal import Link
        
        if isinstance(obj, Link):
            obj_dict = {attr: getattr(obj, attr, None) for attr in dir(obj)
                        if not attr.startswith('_') and not callable(getattr(obj, attr, None))}
            href = obj_dict.get('href', '')
            if 'searchresult:category' in obj_dict.get('rel', ''):
                obj_dict['categoryid'] = href.split('/')[-1]
            elif 'searchresult:event' in obj_dict.get('rel', ''):
                obj_dict['eventid'] = href.split('/')[-1]
            elif 'listconstraints' in obj_dict.get('rel', ''):
                obj_dict['listingconstraintid'] = href.split('/')[-1]
            return obj_dict
        
        elif isinstance(obj, dict):
            return {key: self.object_to_dict(value) for key, value in obj.items()}
        
        elif hasattr(obj, '__dict__'):
            result = {}
            for key, value in obj.__dict__.items():
                if key == 'links':
                    result[key] = {k: self.object_to_dict(v) for k, v in value.items()}
                else:
                    result[key] = self.object_to_dict(value)

                if key == 'notes_html': 
                    soup = BeautifulSoup(value, 'html.parser') 
                    result['notes_text'] = soup.get_text(separator=' ', strip=True)
            return result
        
        elif isinstance(obj, list):
            return [self.object_to_dict(item) for item in obj]       
        else:
            return obj


class DummyFactory:
    """
    A dummy factory that simply returns the raw input item.
    This bypasses the need for a real factory object.
    """
    def __call__(self, item):
        return item

